# 2편 1장 — 에이전트 모델 : 실행 예제 모음
import json, re
import numpy as np

# ── 예제 1. ReAct 루프 : 생각 → 행동 → 관찰을 되풀이 ─────────────────
RATES = {"가은행": 5.4, "나은행": 4.8, "다은행": 5.1}            # 가상의 대출 금리표 (연 %)

def lookup_rates(_):                                          # 도구 1: 금리표 조회
    return ", ".join(f"{k} {v}%" for k, v in RATES.items())

def calculator(expr):                                         # 도구 2: 계산기
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expr):            # 숫자와 연산자만 허용
        return "오류: 계산식이 아님"
    return f"{eval(expr):,.0f}"

TOOLS = {"금리조회": lookup_rates, "계산기": calculator}

def fake_llm(history):
    """설명용 '가짜 LLM'. 실제 LLM이 하는 일을 미리 정한 대본으로 흉내 낸다."""
    n_obs = sum(1 for h in history if h.startswith("관찰"))
    if n_obs == 0:
        return "생각: 금리를 모르니 먼저 은행별 금리를 알아봐야 한다.\n행동: 금리조회[]"
    if n_obs == 1:
        return ("생각: 가장 낮은 금리는 나은행 4.8%. 월 이자율 r=0.048/12=0.004, n=36개월.\n"
                "행동: 계산기[100000000*0.004*(1.004**36)/((1.004**36)-1)]")
    last = history[-1].replace("관찰: ", "")                  # 마지막 관찰을 읽고 답한다
    return f"생각: 계산 결과가 나왔으니 답할 수 있다.\n최종 답: 나은행(연 4.8%), 월 상환액 약 {last}원"

def run_agent(question, max_steps=5):
    history = [f"질문: {question}"]
    for step in range(1, max_steps + 1):
        out = fake_llm(history)
        history.append(out)
        print(f"  [{step}단계] " + out.replace("\n", "\n          "))
        if "최종 답" in out:
            return history
        m = re.search(r"행동: (\S+?)\[(.*)\]", out)
        obs = TOOLS[m.group(1)](m.group(2))                     # 하네스가 도구를 실제로 실행
        history.append(f"관찰: {obs}")
        print(f"          관찰: {obs}")
    return history

print("[예제 1] ReAct 에이전트")
run_agent("1억 원을 3년(36개월) 원리금 균등으로 빌리려 한다. 가장 싼 은행과 월 상환액은?")

# ── 예제 2. 여러 단계 일의 성공 확률 : 작은 실수가 쌓인다 ───────────────
print("\n[예제 2] 한 단계 성공률 p, 단계 수 k 일 때 끝까지 성공할 확률")
print("    p     k=5   k=10   k=20   k=50  | 검산 후 재시도 (k=20)")
for p in [0.90, 0.95, 0.99]:
    plain = [p ** k for k in [5, 10, 20, 50]]
    d = 0.8                                                     # 실수를 알아챌 확률
    p_retry = p + (1 - p) * d * p                               # 알아채면 한 번 더 시도
    print(f"  {p:.2f} " + " ".join(f"{x:6.1%}" for x in plain) + f"  | {p_retry ** 20:6.1%}")

# ── 예제 3. 어떤 도구를 쓸지 보상으로 배우기 (4장 강화학습의 재등장) ──────
KINDS = ["계산 문제", "최신 정보", "일반 상식"]
TOOLN = ["바로 답", "계산기", "검색"]
SUCCESS = np.array([[0.40, 0.95, 0.30],        # 계산 문제: 계산기가 가장 잘 맞힘
                    [0.10, 0.05, 0.90],        # 최신 정보: 검색만 통함
                    [0.85, 0.10, 0.80]])       # 일반 상식: 바로 답해도 됨 (도구는 시간 낭비)
COST = np.array([0.0, 0.05, 0.10])             # 도구를 부르면 시간·비용 감점
rng = np.random.default_rng(0)
theta = np.zeros((3, 3))
for t in range(3000):
    k = rng.integers(3)
    pi = np.exp(theta[k]) / np.exp(theta[k]).sum()
    a = rng.choice(3, p=pi)
    reward = float(rng.random() < SUCCESS[k, a]) - COST[a]      # 일을 끝냈나? (규칙 채점)
    baseline = pi @ (SUCCESS[k] - COST)
    grad = -pi; grad[a] += 1
    theta[k] += 0.1 * (reward - baseline) * grad
print("\n[예제 3] 3,000번 연습 뒤 문제 종류별 도구 선택 확률")
print("              바로 답  계산기   검색")
for k, name in enumerate(KINDS):
    pi = np.exp(theta[k]) / np.exp(theta[k]).sum()
    print(f"  {name:8s} " + " ".join(f"{x:7.0%}" for x in pi))

P, r, n = 100_000_000, 0.004, 36
print(f"\n검산: 월 상환액 = {P * r * (1 + r) ** n / ((1 + r) ** n - 1):,.0f}원")
