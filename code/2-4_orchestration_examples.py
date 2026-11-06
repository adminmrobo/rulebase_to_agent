# 2편 4장 — 오케스트레이션 : 실행 예제 모음
import time
from concurrent.futures import ThreadPoolExecutor

# ── 예제 1. 지휘자와 서브에이전트 : 나눠서 동시에 ─────────────────────
SUBTASKS = {  # 서브에이전트 이름: (맡은 일, 걸리는 시간(초) — 설명용으로 짧게)
    "조수(하루)":     ("금리·환율 데이터 수집", 0.6),
    "Money-Robo":     ("수익률 계산과 표 작성", 0.5),
    "초파리 연구원":  ("관련 뉴스 3건 요약", 0.7),
}

def subagent(name, job, sec):
    time.sleep(sec)                                   # 실제로는 LLM이 도구를 쓰며 일하는 시간
    return f"[{name}] {job} 완료 (요약 3줄만 보고)"   # 지휘자에게는 짧은 요약만 넘김

def orchestrator(parallel=True):
    t0 = time.time()
    if parallel:
        with ThreadPoolExecutor() as ex:
            reports = list(ex.map(lambda kv: subagent(kv[0], *kv[1]), SUBTASKS.items()))
    else:
        reports = [subagent(n, j, s) for n, (j, s) in SUBTASKS.items()]
    return reports, time.time() - t0

print("[예제 1] 지휘자(박사)가 주간 시장 보고서를 나눠 맡김")
for mode in (False, True):
    reports, sec = orchestrator(parallel=mode)
    print(f"  {'동시에' if mode else '차례로'}: {sec:.2f}초")
for r in reports:
    print("   ", r)

# ── 예제 2. 언제 나누는 게 이득일까? (계산 모형) ──────────────────────
# 가정: 하위 작업 6개. 모두 맞아야 보고서 성공.
#  · 혼자 하기: 기록이 쌓일수록 실수 증가 e_i = 0.04 + 0.025·i, 스스로 검토는 실수의 30%만 잡음
#  · 나눠 하기: 매번 새 컨텍스트라 실수 0.04, 대신 작업끼리 얽힌 정도 c 만큼 인수인계 손실 0.15·c,
#               독립 검증 에이전트가 실수의 70%를 잡아 한 번 다시 시킴
#  · 토큰: 서브에이전트는 각자 검색·탐색을 하므로 하나당 2만 토큰 (앤트로픽이 밝힌 '에이전트 약 4배,
#          멀티에이전트 약 15배'와 비슷한 비율이 되도록 정한 가정)
def solo(n=6, catch=0.3):
    p = 1.0
    for i in range(n):
        e = 0.04 + 0.025 * i
        p *= 1 - e * (1 - catch + catch * e)          # 못 잡았거나, 잡아서 다시 했는데 또 틀림
    return p, n, sum(2000 * (i + 1) for i in range(n))    # 성공률, 시간, 토큰

def team(c, n=6, catch=0.7):
    e = 0.04 + 0.15 * c
    p = (1 - e * (1 - catch + catch * e)) ** n
    waves = 1 + round(c * (n - 1))                    # 얽혀 있을수록 기다렸다 해야 함
    time_ = 1 + waves + 1                             # 계획 + 실행 + 취합
    tokens = n * 20000 + 6000 + n * 1500 + n * 4000 * c  # 서브에이전트(각자 탐색) + 지휘자 + 검증 + 맥락 공유
    return p, time_, tokens

print("\n[예제 2] 혼자 하기 vs 나눠 하기 (작업끼리 얽힌 정도 c)")
p, t, k = solo()
print(f"  혼자 하기          성공 {p:5.1%}  시간 {t:4.1f}  토큰 {k:7,.0f}")
for c in [0.0, 0.25, 0.5, 0.75, 1.0]:
    p, t, k = team(c)
    print(f"  나눠 하기 c={c:.2f}  성공 {p:5.1%}  시간 {t:4.1f}  토큰 {k:7,.0f}  ({k / solo()[2]:.1f}배)")
