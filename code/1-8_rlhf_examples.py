# 1편 8장 — RLHF : 실행 예제 모음
import json
import numpy as np

sig = lambda z: 1 / (1 + np.exp(-z))
PROMPT = "금리가 오르면 채권 가격은 어떻게 되나요?"
ANS = {
    "A": "금리가 내리면 채권 가격은 어떻게 되나요? 환율이 오르면 주가는 어떻게 되나요?",
    "B": "보통 내립니다. 이미 나온 채권의 고정 이자가 새로 나오는 채권보다 덜 매력적이 되기 때문입니다.",
    "C": "보통 내립니다. 예를 들어 연 3% 이자를 주는 채권을 갖고 있는데 시장 금리가 5%로 오르면, "
         "누구도 3% 채권을 제값에 사려 하지 않으니 가격을 낮춰야 팔립니다. 만기가 길수록 더 많이 내립니다.",
    "D": "채권 가격도 함께 오릅니다. 금리가 높을수록 채권이 인기를 얻기 때문입니다.",
    "E": "정말 훌륭한 질문이세요! 이런 질문을 하시는 걸 보니 투자 감각이 대단하십니다. 금융 시장은 "
         "매우 복잡하고 다양한 요인이 서로 얽혀 있어서 한마디로 말하기는 어렵지만, 여러 전문가들의 "
         "견해와 역사적 사례를 폭넓게 살펴보면 일반적으로는 가격이 내리는 경향이 있다고 할 수 있습니다. "
         "항상 신중하게 판단하시길 바랍니다!",
}
KEYS = list(ANS)
GOLD = np.array([-1.5, 1.5, 2.0, -2.5, 0.5])       # 진짜 품질 (우리가 바라는 것)
LEN = np.array([len(ANS[k]) for k in KEYS]) / 100  # 길이 (100자 단위)
P_REF = np.array([0.40, 0.15, 0.10, 0.20, 0.15])    # 사전학습 모델이 원래 고르던 확률

# ── 예제 1. 사람의 비교로 보상모델 만들기 (브래들리-테리) ─────────────
rng = np.random.default_rng(0)
LENGTH_BIAS = 1.0                                    # 라벨러가 긴 답을 조금 더 좋아하는 버릇
FLATTER_BIAS = 2.0                                   # 칭찬받으면 기분이 좋아지는 버릇
FLATTER = np.array([0, 0, 0, 0, 1])                  # 칭찬이 들어 있는 답은 E뿐
seen = GOLD + LENGTH_BIAS * LEN + FLATTER_BIAS * FLATTER   # 라벨러 눈에 보이는 좋음
pairs = []
for _ in range(600):                                 # 비교 600번
    i, j = rng.choice(5, 2, replace=False)
    p_i = sig(seen[i] - seen[j])
    pairs.append((i, j) if rng.random() < p_i else (j, i))   # (이긴 답, 진 답)

r = np.zeros(5)
for _ in range(2000):                                # −log σ(r_w − r_l) 를 줄이는 경사하강
    g = np.zeros(5)
    for w, l in pairs:
        d = 1 - sig(r[w] - r[l])
        g[w] -= d; g[l] += d
    r -= 0.05 * g / len(pairs)
r -= r.mean()
print("[예제 1] 비교 600번으로 배운 보상 r (평균 0으로 맞춤)")
for k, rv, gv in zip(KEYS, r, GOLD - GOLD.mean()):
    print(f"  답 {k}: 보상모델 {rv:+.2f}   진짜 품질 {gv:+.2f}   ({len(ANS[k])}자)")

# ── 예제 2. KL 고삐를 단 최적 정책 π*(y) ∝ π_ref(y)·exp(r(y)/β) ─────
def policy(beta):
    w = P_REF * np.exp(r / beta)
    return w / w.sum()
print("\n[예제 2] 고삐 β 에 따른 정책 (답 A~E를 고를 확률)")
print("    β     A     B     C     D     E    KL    보상모델  진짜 품질")
for beta in [100, 3, 1.5, 1, 0.7, 0.5, 0.3, 0.1]:
    pi = policy(beta)
    kl = float(np.sum(pi * np.log(pi / P_REF)))
    print(f"  {beta:5.2f} " + " ".join(f"{p:5.2f}" for p in pi)
          + f"  {kl:5.2f}   {pi @ r:+6.2f}    {pi @ GOLD:+6.2f}")

json.dump({"prompt": PROMPT, "keys": KEYS, "ans": ANS, "gold": GOLD.tolist(),
           "len": LEN.tolist(), "pref": P_REF.tolist(), "bias": LENGTH_BIAS, "fbias": FLATTER_BIAS, "flatter": FLATTER.tolist(),
           "r": [round(float(x), 3) for x in r], "pairs": pairs[:40]},
          open("ch08_data.json", "w"), ensure_ascii=False, default=int)
