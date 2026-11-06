# 2편 5장 — 자가개선 루프 : 실행 예제 모음
# 상황: Money-Robo가 매일 반복 업무 8종 중 하나를 에이전트에게 맡긴다. 숫자는 설명용 가정.
import numpy as np

TASKS = ["주간 시장 보고서", "장부 대사", "뉴스 요약", "고객 문의 답장",
         "환율 알림", "회의록 정리", "SEO 점검", "월말 정산표"]

def day_result(rng, skill):
    """스킬 상태에 따라 오늘 일의 성공 여부와 비용(토큰·시간)을 정한다."""
    if skill is None:                     p, cost = 0.55, 10.0          # 매번 처음부터 시행착오
    elif skill["bad"]:                    p, cost = 0.35, 6.0           # 잘못 배운 절차를 그대로 따라 함
    else:
        q = skill["q"]
        p, cost = 0.55 + 0.4 * q, 10.0 - 6.0 * q                         # 좋은 스킬일수록 빠르고 정확
    return rng.random() < p, cost

def simulate(policy, days=90, seed=0, snap=None):
    rng = np.random.default_rng(seed)
    skills, log = {}, []
    for d in range(days):
        if snap is not None: snap.append({k: dict(v) for k, v in skills.items()})
        t = int(rng.integers(len(TASKS)))
        sk = skills.get(t)
        ok, cost = day_result(rng, sk)
        looks_ok = ok or rng.random() < 0.3                              # 실패해도 30%는 "된 것 같다"
        if policy == "자기 판단으로 저장":
            if looks_ok and sk is None:
                skills[t] = {"q": 0.5, "bad": not ok}                     # 거짓 성공도 스킬로 굳어짐
            elif looks_ok and sk and not sk["bad"]:
                sk["q"] = min(1.0, sk["q"] + 0.1)
        elif policy == "검증 후 저장 + 실패 분석":
            if ok and sk is None:
                skills[t] = {"q": 0.5, "bad": False}                     # 검증을 통과한 절차만 저장
            elif ok and sk:
                sk["q"] = min(1.0, sk["q"] + 0.1)                         # 쓸 때마다 다듬음
            elif not ok and sk:
                if sk["bad"]: del skills[t]                               # 실패 분석: 틀린 스킬은 폐기
                else: sk["q"] = min(1.0, sk["q"] + 0.05)                  # 실패 원인을 스킬에 덧붙임
        log.append((ok, cost))
    return log, skills

print("[예제 1] 90일 동안의 결과 (같은 날 같은 일, 정책만 다름 · 200번 평균)")
print("  정책                      앞 30일 성공  뒤 30일 성공  뒤 30일 평균 비용  저장된 스킬")
for policy in ["스킬 없음", "자기 판단으로 저장", "검증 후 저장 + 실패 분석"]:
    first, last, cost, nsk, nbad = [], [], [], [], []
    for s in range(200):
        log, skills = simulate(policy, seed=s)
        first.append(np.mean([o for o, _ in log[:30]])); last.append(np.mean([o for o, _ in log[-30:]]))
        cost.append(np.mean([c for _, c in log[-30:]]))
        nsk.append(len(skills)); nbad.append(sum(v["bad"] for v in skills.values()))
    print(f"  {policy:22s}  {np.mean(first):8.1%}     {np.mean(last):8.1%}      {np.mean(cost):6.1f}"
          f"         {np.mean(nsk):.1f}개 (잘못된 것 {np.mean(nbad):.1f}개)")

print("\n[예제 2] 30일째 아침의 스킬 서랍 (같은 날짜, 두 정책 비교)")
for policy in ["자기 판단으로 저장", "검증 후 저장 + 실패 분석"]:
    snaps = []
    simulate(policy, seed=1, snap=snaps)
    drawer = snaps[30]
    label = lambda v: "잘못됨" if v["bad"] else f"q={v['q']:.1f}"
    items = [f"{TASKS[t]}({label(v)})" for t, v in sorted(drawer.items())]
    print(f"  {policy}: " + ", ".join(items))
