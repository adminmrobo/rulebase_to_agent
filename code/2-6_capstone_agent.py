# 2편 6장 — 마무리 : 1·2편의 부품을 한 파일에 조립하기
# 상황: Money-Robo의 "대출 상담 에이전트". 고객과 숫자는 모두 가상의 예.
import numpy as np
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(0)

# ① 1편 2장 · 학습된 모델 : 과거 대출 400건(가상)으로 "연체 확률"을 배운다
X = np.c_[rng.normal(5000, 1500, 400), rng.uniform(0, 0.8, 400)]          # 연소득(만 원), 부채비율
y = (rng.random(400) < 1 / (1 + np.exp(-(-2 - 0.0006 * (X[:, 0] - 5000) + 4 * X[:, 1])))).astype(int)
model = LogisticRegression(max_iter=1000).fit((X - X.mean(0)) / X.std(0), y)
def default_prob(income, debt_ratio):
    z = (np.array([[income, debt_ratio]]) - X.mean(0)) / X.std(0)
    return float(model.predict_proba(z)[0, 1])

# ② 1편 1장 · 규칙 : 사람이 쓴 IF-THEN. 이번에는 판단이 아니라 '문지기'
def gate(amount, prob):
    if amount > 50_000_000: return "차단", "한도 5천만 원 초과"
    if prob > 0.40:         return "사람 심사", "연체확률 40% 초과"
    return "통과", "규칙 2개 모두 통과"

# 에이전트가 알고 있는 계산 절차 두 가지 (하나는 틀린 방법)
PROCS = {
    "단리 나눗셈": lambda a, rate, m: a * (1 + rate * m / 12) / m,                       # 틀림
    "원리금균등":  lambda a, rate, m: a * (rate / 12) * (1 + rate / 12) ** m / ((1 + rate / 12) ** m - 1),
}

# ③ 2편 3장 · 검증기 : 에이전트의 말이 아니라, 독립된 계산으로 다시 확인
def verify(answer, amount, rate, months):
    r = rate / 12
    truth = amount * r * (1 + r) ** months / ((1 + r) ** months - 1)
    return abs(answer - truth) < 1

# 가짜 에이전트 (설명용): 저장된 스킬이 있으면 그 절차를, 없으면 첫 시도는 익숙한 단리로, 다음엔 다른 방법으로
def agent_try(skills, attempt):
    if "월 상환액" in skills: return skills["월 상환액"]
    return "단리 나눗셈" if attempt == 0 else "원리금균등"

# ④⑤ 2편 1·3·5장 · 에이전트 루프 + 스킬 기억. policy에 따라 저장 기준이 다르다
def run(policy):
    skills, log = {}, []
    for name, income, debt, amount, rate, months in CUSTOMERS:
        p = default_prob(income, debt)
        decision, why = gate(amount, p)
        if decision != "통과":
            log.append(f"{name}: {decision:5s} │ 근거: 연체확률 {p:.0%}, {why}"); continue
        for attempt in range(3):
            proc = agent_try(skills, attempt)
            pay = PROCS[proc](amount, rate, months)
            ok = verify(pay, amount, rate, months)
            if policy == "검증 후 저장" and not ok:
                continue                                         # 틀리면 다시 (저장 안 함)
            if "월 상환액" not in skills:
                skills["월 상환액"] = proc                        # 에이전트가 방금 쓴 절차를 스킬로 기록
            mark = "맞음" if ok else "틀림"
            log.append(f"{name}: 월 {pay:>11,.0f}원 [{mark}] │ 근거: 연체확률 {p:.0%}, 절차 '{proc}', 시도 {attempt + 1}회")
            break
        else:
            log.append(f"{name}: 사람에게 │ 근거: 검증 3회 실패")
    return log, skills

CUSTOMERS = [("고객 A", 6500, 0.20, 30_000_000, 0.048, 36),
             ("고객 B", 3000, 0.75, 20_000_000, 0.051, 24),
             ("고객 C", 5200, 0.30, 80_000_000, 0.048, 60),
             ("고객 D", 4800, 0.25, 15_000_000, 0.054, 12),
             ("고객 E", 7000, 0.10, 40_000_000, 0.048, 48)]

print("[마무리 실험] 같은 고객 5명, 스킬 저장 기준만 다르게")
for policy in ["검증 후 저장", "검증 없이 저장"]:
    log, skills = run(policy)
    print(f"\n■ {policy} → 저장된 스킬: {skills}")
    for line in log: print("  " + line)
