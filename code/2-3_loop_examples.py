# 2편 3장 — 루프 엔지니어링 : 실행 예제 모음
# 상황: 코딩 에이전트가 실패하는 테스트(버그 5개)를 고치는 루프. 숫자는 설명용 가정.
import numpy as np

def run_loop(rng, verifier=True, max_iter=30, budget=40.0, patience=6, reflect=False, log=False):
    bugs, cost, best, stall, lessons = 5, 0.0, 5, 0, 0
    for it in range(1, max_iter + 1):
        p_fix = min(0.6, 0.30 + 0.06 * lessons)                # 반성 메모가 쌓이면 고칠 확률 ↑
        p_break = max(0.02, 0.10 - 0.015 * lessons)            # 같은 실수를 덜 반복
        if rng.random() < p_fix and bugs > 0: bugs -= 1        # 행동: 하나 고침
        if rng.random() < p_break: bugs += 1                   # 부작용: 다른 곳이 깨짐
        cost += 1 + 0.08 * it                                  # 반복할수록 기록이 쌓여 비용 증가
        if log: print(f"    {it:2d}회: 남은 버그 {bugs}, 누적 비용 {cost:5.1f}")
        # ── 멈춤 판단 ─────────────────────────────
        if verifier and bugs == 0:
            return "진짜 완료", it, cost                        # 외부 검증기(테스트)가 통과 확인
        if not verifier:
            claim = 0.6 if bugs == 0 else 0.12                 # 에이전트의 자기 보고 "다 됐어요"
            if rng.random() < claim:
                return ("진짜 완료" if bugs == 0 else "거짓 완료"), it, cost
        if bugs < best: best, stall = bugs, 0
        else:
            stall += 1
            if reflect: lessons += 1                           # 실패를 글로 반성해 기억에 남김
        if stall >= patience: return "진전 없음 → 사람에게", it, cost
        if cost >= budget:    return "예산 소진 → 사람에게", it, cost
    return "반복 한도 → 사람에게", max_iter, cost

print("[예제 1] 루프 한 번 따라가 보기 (검증기 켬)")
print("  결과:", run_loop(np.random.default_rng(3), log=True))

def evaluate(name, n=4000, **kw):
    rng = np.random.default_rng(0)
    res = [run_loop(rng, **kw) for _ in range(n)]
    share = lambda key: sum(r[0].startswith(key) for r in res) / n
    print(f"  {name:20s} 진짜완료 {share('진짜'):5.1%}  거짓완료 {share('거짓'):5.1%}  "
          f"진전없음 {share('진전'):5.1%}  예산·한도 {share('예산') + share('반복'):5.1%}  "
          f"평균비용 {np.mean([r[2] for r in res]):5.1f}")

print("\n[예제 2] 루프 설계별 결과 (4,000번 모의실험)")
evaluate("자기 보고로 멈춤", verifier=False)
evaluate("검증기로 멈춤", verifier=True)
evaluate("검증기 + 예산 2배", verifier=True, budget=80.0, max_iter=60)
evaluate("검증기 + 반성 메모", verifier=True, reflect=True)
