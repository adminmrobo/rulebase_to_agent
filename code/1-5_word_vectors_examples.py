# 1편 5장 — 말을 숫자로 바꾸다 : 실행 예제 모음
import json, random
from collections import Counter, defaultdict
import numpy as np

# ── 예제 1. 바이그램 언어모델 : 앞 단어 하나로 다음 단어 맞히기 ──────────
CORPUS = """
박사 는 물고기 를 잰다 .
조수 는 물고기 를 기록 한다 .
조수 는 데이터 를 기록 한다 .
박사 는 데이터 를 믿는다 .
로봇 은 데이터 를 믿는다 .
로봇 은 금화 를 좋아한다 .
초파리 는 데이터 를 의심 한다 .
초파리 는 로봇 을 의심 한다 .
박사 는 이론 을 좋아한다 .
조수 는 실험 을 좋아한다 .
로봇 은 미로 를 달린다 .
로봇 은 출구 를 찾는다 .
조수 는 미로 를 그린다 .
박사 는 규칙 을 쓴다 .
기계 는 규칙 을 따른다 .
기계 는 데이터 를 배운다 .
기계 는 보상 을 배운다 .
초파리 는 실험 을 좋아한다 .
""".split()

bigram = defaultdict(Counter)
for w1, w2 in zip(CORPUS, CORPUS[1:]):
    if w1 != ".":
        bigram[w1][w2] += 1

def next_probs(word):
    c = bigram[word]
    total = sum(c.values())
    return {w: n / total for w, n in c.most_common()}

print("[예제 1] 바이그램 확률표 일부")
for w in ["로봇", "데이터", "를"]:
    probs = ", ".join(f"{k} {v:.0%}" for k, v in list(next_probs(w).items())[:4])
    print(f"  P(다음 | {w}) → {probs}")

random.seed(3)
def generate(start, n=8):
    out = [start]
    while len(out) < n and out[-1] != ".":
        p = next_probs(out[-1])
        out.append(random.choices(list(p), weights=list(p.values()))[0])
    return " ".join(out)
print("  생성한 문장:")
for s in ["로봇", "초파리", "박사"]:
    print("   ", generate(s))

# ── 예제 2. 원-핫 벡터는 왜 뜻을 담지 못하나 ──────────────────
vocab = ["강아지", "강아지새끼", "머핀"]
onehot = np.eye(len(vocab))
cos = lambda a, b: float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
print("\n[예제 2] 원-핫 벡터의 코사인 유사도")
print(f"  강아지·강아지새끼 {cos(onehot[0], onehot[1]):.2f} / 강아지·머핀 {cos(onehot[0], onehot[2]):.2f}")

# ── 예제 3. 실제 단어 벡터 (GloVe, 40만 단어 × 50차원) ──────────
from gensim.models import KeyedVectors
kv = KeyedVectors.load("data/glove50.kv")
print("\n[예제 3] GloVe 단어 벡터")
print(f"  dog·puppy {kv.similarity('dog', 'puppy'):.3f} / dog·muffin {kv.similarity('dog', 'muffin'):.3f}"
      f" / muffin·cake {kv.similarity('muffin', 'cake'):.3f}")
for pos, neg in [(["king", "woman"], ["man"]), (["paris", "korea"], ["france"]),
                 (["bigger", "small"], ["big"]), (["walking", "swam"], ["walked"])]:
    top = kv.most_similar(positive=pos, negative=neg, topn=3)
    print(f"  {pos[0]} − {neg[0]} + {pos[1]} → " + ", ".join(f"{w} {s:.3f}" for w, s in top))
print("  bank 와 가까운 단어:", ", ".join(w for w, _ in kv.most_similar("bank", topn=6)))

# ── 예제 4. 토큰 나누기 : 바이트 쌍 인코딩(BPE) 맛보기 ──────────────
words = Counter({"l o w _": 5, "l o w e r _": 2, "n e w e s t _": 6, "w i d e s t _": 3})
print("\n[예제 4] BPE : 가장 자주 붙어 나오는 글자 쌍을 하나로 합치기")
for step in range(1, 6):
    pairs = Counter()
    for w, n in words.items():
        sym = w.split()
        for a, b in zip(sym, sym[1:]):
            pairs[a, b] += n
    (a, b), cnt = pairs.most_common(1)[0]
    words = Counter({w.replace(f"{a} {b}", a + b): n for w, n in words.items()})
    print(f"  {step}번째 합치기: '{a}' + '{b}' ({cnt}번) → {list(words)}")

# 페이지용 데이터 저장
WORDS = ["king", "queen", "man", "woman", "prince", "princess",
         "paris", "france", "seoul", "korea", "tokyo", "japan", "beijing", "china",
         "dog", "puppy", "cat", "kitten", "muffin", "cake", "bread", "cookie",
         "bank", "money", "stock", "loan", "market", "investor",
         "big", "bigger", "small", "smaller", "robot", "machine", "computer", "fish"]
vecs = np.array([kv[w] for w in WORDS])
c = vecs - vecs.mean(0)
_, _, vt = np.linalg.svd(c, full_matrices=False)
xy = c @ vt[:2].T
json.dump({"bigram": {k: dict(v) for k, v in bigram.items()},
           "words": WORDS,
           "vec": [[round(float(x), 4) for x in kv[w]] for w in WORDS],
           "xy": [[round(float(a), 3), round(float(b), 3)] for a, b in xy]},
          open("ch05_data.json", "w"), ensure_ascii=False)
