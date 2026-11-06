# 1편 6장 — 트랜스포머와 어텐션 : 실행 예제 모음
import json
import numpy as np
from gensim.models import KeyedVectors

np.set_printoptions(precision=2, suppress=True)
softmax = lambda s: np.exp(s - s.max(-1, keepdims=True)) / np.exp(s - s.max(-1, keepdims=True)).sum(-1, keepdims=True)

# ── 예제 1. 셀프 어텐션 10줄 ───────────────────────────────
def self_attention(X, Wq, Wk, Wv, mask=None):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv          # 질문 · 꼬리표 · 내용
    S = Q @ K.T / np.sqrt(K.shape[1])          # 모든 단어 쌍의 관련도
    if mask is not None:
        S = np.where(mask, S, -1e9)             # 보면 안 되는 칸은 지움
    A = softmax(S)                              # 줄마다 합이 1인 가중치
    return A @ V, A

rng = np.random.default_rng(0)
X = rng.normal(size=(4, 8))                     # 단어 4개, 각 8차원
Wq, Wk, Wv = (rng.normal(size=(8, 8)) for _ in range(3))
out, A = self_attention(X, Wq, Wk, Wv)
print("[예제 1] 어텐션 가중치 (줄 = 보는 단어, 칸 = 보이는 단어)")
print(A)
print("  줄마다 합:", A.sum(1))

# ── 예제 2. 다음 단어 예측용 '미래 가리기' 마스크 ───────────────
causal = np.tril(np.ones((4, 4), dtype=bool))
_, A2 = self_attention(X, Wq, Wk, Wv, mask=causal)
print("\n[예제 2] 인과 마스크를 씌운 가중치 (앞 단어만 볼 수 있음)")
print(A2)

# ── 예제 3. 문맥이 바꾸는 bank의 뜻 (GloVe 벡터 + 어텐션) ──────────
kv = KeyedVectors.load("data/glove50.kv")
S1 = "he sat on the river bank and watched the water".split()
S2 = "she went to the bank to get a loan and some money".split()
FUNC = {"he", "she", "on", "the", "and", "to", "a", "some", "get", "went", "sat", "watched"}
cos = lambda a, b: float(a @ b / np.linalg.norm(a) / np.linalg.norm(b))

def bank_in_context(sent, focus_content):
    Xs = np.array([kv[w] for w in sent])
    i = sent.index("bank")
    s = Xs @ Xs[i] / np.sqrt(Xs.shape[1])        # bank가 다른 단어를 보는 점수
    s[i] = -1e9                                   # 자기 자신은 빼고
    if focus_content:                             # 학습된 W_Q, W_K가 하는 일을 손으로 흉내:
        s = np.where([w in FUNC for w in sent], -1e9, s)   # 기능어는 보지 않음
    w = softmax(s)
    return Xs[i] + w @ Xs, w                      # 잔차 연결: 원래 뜻 + 문맥

print("\n[예제 3] bank의 뜻이 문맥에 따라 움직이나? (river 유사도 − money 유사도)")
b = kv["bank"]
print(f"  고정 벡터(5장)        : {cos(b, kv['river']) - cos(b, kv['money']):+.3f}")
for label, focus in [("학습 전 어텐션", False), ("내용어에 집중", True)]:
    for name, S in [("강가 문장", S1), ("대출 문장", S2)]:
        v, w = bank_in_context(S, focus)
        top = ", ".join(f"{t} {x:.2f}" for t, x in sorted(zip(S, w), key=lambda t: -t[1])[:3])
        print(f"  {label} · {name}: {cos(v, kv['river']) - cos(v, kv['money']):+.3f}   많이 본 단어: {top}")
for name, S in [("강가 문장", S1), ("대출 문장", S2)]:
    v, _ = bank_in_context(S, True)
    near = [w for w, _ in kv.similar_by_vector(v, topn=8) if w not in ("bank", "banks")][:5]
    print(f"  {name}의 bank와 가까운 단어 (40만 단어 중): {', '.join(near)}")

# ── 예제 4. 위치 인코딩 : 단어 순서를 숫자로 ──────────────────
def positional_encoding(n_pos, d):
    pos = np.arange(n_pos)[:, None]
    i = np.arange(d // 2)[None, :]
    ang = pos / (10000 ** (2 * i / d))
    pe = np.zeros((n_pos, d))
    pe[:, 0::2], pe[:, 1::2] = np.sin(ang), np.cos(ang)
    return pe
PE = positional_encoding(6, 8)
print("\n[예제 4] 위치 인코딩 (위치 0~5, 앞 4차원)")
print(PE[:, :4])

# 페이지용 데이터
words = sorted(set(S1 + S2 + ["river", "water", "shore", "money", "loan", "finance"]))
json.dump({"s1": S1, "s2": S2, "func": sorted(FUNC),
           "vec": {w: [round(float(x), 4) for x in kv[w]] for w in words}},
          open("ch06_data.json", "w"))
