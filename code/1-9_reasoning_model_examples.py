# 1편 9장 — 추론 모델 : 실행 예제 모음
import json, re
import numpy as np

# ── 예제 1. 규칙 채점기 : 1장의 IF-THEN이 심판으로 돌아오다 ──────────
def rule_reward(response, answer):
    r = 0.0
    if re.search(r"<think>.+</think>", response, re.S):        # 형식 규칙: 생각을 태그 안에
        r += 0.1
    m = re.search(r"답:\s*(-?\d+)", response)                   # 마지막 '답: 숫자'를 꺼내
    if m and int(m.group(1)) == answer:                          # 정답과 같으면
        r += 1.0
    return r

Q, ANSWER = "사과 23개가 든 상자 4개에서 17개를 먹었다. 남은 사과는?", 75
cands = {
    "바로 답":      "답: 82",
    "풀이 후 답":   "<think>23×4=92, 92−17=75</think> 답: 75",
    "풀이 틀림":    "<think>23×4=82, 82−17=65</think> 답: 65",
    "형식 무시":    "23 곱하기 4는 92이고 17을 빼면 75. 답: 75",
}
print("[예제 1] 규칙 채점기의 점수")
for name, resp in cands.items():
    print(f"  {name:8s} → {rule_reward(resp, ANSWER):.1f}")

# ── 예제 2. 여러 번 풀고 다수결 (자기일관성) ───────────────────
rng = np.random.default_rng(0)
def vote_accuracy(p, n, n_wrong=4, trials=20000):
    ok = 0
    for _ in range(trials):
        right = rng.random(n) < p
        votes = np.zeros(n_wrong + 1)
        votes[0] = right.sum()
        wrong_ans = rng.integers(1, n_wrong + 1, size=(~right).sum())
        np.add.at(votes, wrong_ans, 1)
        best = np.flatnonzero(votes == votes.max())
        ok += rng.choice(best) == 0                     # 동점이면 무작위
    return ok / trials
print("\n[예제 2] 한 번 풀 때 정답률 p, n번 풀어 다수결")
print("    p     n=1    n=5   n=15   n=64")
for p in [0.3, 0.5, 0.7]:
    print(f"  {p:.1f} " + " ".join(f"{vote_accuracy(p, n, trials=4000):6.1%}" for n in [1, 5, 15, 64]))

# ── 예제 3. 규칙 보상만으로 '생각하는 습관' 기르기 (GRPO 장난감) ──────
STRAT = ["바로 답", "한 단계씩", "한 단계씩 + 검산", "같은 말 반복"]
ACC   = np.array([0.30, 0.65, 0.90, 0.45])     # 전략별 정답 확률
LENG  = np.array([10,   80,   160,  300])      # 전략별 풀이 길이(토큰)
FMT   = np.array([0,    1,    1,    1])        # <think> 형식을 지키는가
G, lr = 8, 0.3                                  # 한 문제를 8번 풀어 모둠 비교

def train(seed, steps=400, record=False):
    rg = np.random.default_rng(seed)
    theta = np.array([2.0, 0.0, -1.5, 0.0])     # 처음엔 '바로 답' 습관이 강하고 '검산'은 드묾
    hist = []
    for step in range(steps + 1):
        pi = np.exp(theta) / np.exp(theta).sum()
        if record and step % 25 == 0:
            hist.append([step] + [round(float(x), 3) for x in pi]
                        + [round(float(pi @ LENG), 1), round(float(pi @ ACC), 3)])
        picks = rg.choice(4, size=G, p=pi)                          # 같은 문제를 8번 풀고
        rewards = (rg.random(G) < ACC[picks]) * 1.0 + 0.1 * FMT[picks]   # 규칙으로 채점
        adv = (rewards - rewards.mean()) / (rewards.std() + 1e-8)   # 모둠 평균 대비 상대 점수
        for a, A in zip(picks, adv):
            grad = -pi.copy(); grad[a] += 1                         # log π(a)의 기울기
            theta += lr * A * grad / G
    return pi, hist

_, hist = train(seed=1, record=True)
print("\n[예제 3] GRPO 장난감 학습 : 전략별 선택 확률, 평균 풀이 길이, 정답률")
print("  단계   바로답  한단계  +검산   반복   길이  정답률")
for h in hist:
    if h[0] % 50 == 0:
        print(f"  {h[0]:4d}  " + "  ".join(f"{x:5.2f}" for x in h[1:5]) + f"  {h[5]:5.0f}  {h[6]:5.1%}")
found = sum(train(sd)[0][2] > 0.5 for sd in range(1, 11))
print(f"  처음부터 10번 다시 학습: '검산' 습관에 도달 {found}/10")

json.dump({"strat": STRAT, "acc": ACC.tolist(), "len": LENG.tolist(), "hist": hist},
          open("ch09_data.json", "w"), ensure_ascii=False)
