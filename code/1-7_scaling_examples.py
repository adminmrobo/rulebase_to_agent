# 1편 7장 — 스케일링 : 실행 예제 모음
import json, warnings
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import log_loss
warnings.filterwarnings("ignore")

# ── 예제 1. 우리 실험실의 작은 스케일링 법칙 : 데이터를 늘리면 손실은? ──
digits = load_digits()
Xtr, Xte, ytr, yte = train_test_split(digits.data / 16, digits.target, test_size=450,
                                      random_state=0, stratify=digits.target)
sizes = [40, 80, 160, 320, 640, 1280]
losses = []
print("[예제 1] 학습 데이터 크기별 시험 손실 (손글씨 숫자, 3번 평균)")
for n in sizes:
    ls = []
    for seed in range(3):
        m = MLPClassifier(hidden_layer_sizes=(64,), alpha=1e-3, max_iter=2000,
                          random_state=seed).fit(Xtr[:n], ytr[:n])
        ls.append(log_loss(yte, m.predict_proba(Xte), labels=range(10)))
    losses.append(np.mean(ls))
    print(f"  데이터 {n:5d}장 → 시험 손실 {losses[-1]:.3f}")
slope, icpt = np.polyfit(np.log10(sizes), np.log10(losses), 1)
print(f"  로그-로그 직선 맞추기: 손실 ∝ 데이터^{slope:.3f}  (데이터 2배 → 손실 ×{2**slope:.3f})")

# ── 예제 2. 카플란 법칙으로 계산해 보기 ─────────────────────────
aN, Nc = 0.076, 8.8e13
print("\n[예제 2] L(N) = (Nc/N)^0.076 : 모델을 10배 키울 때마다")
print(f"  손실 × {10**-aN:.3f}  (약 {1-10**-aN:.0%}씩 줄어듦)")
for name, N in [("GPT-1", 117e6), ("GPT-2", 1.5e9), ("GPT-3", 175e9)]:
    print(f"  {name:6s} 파라미터 {N:9.3g} → 공식상 손실 {(Nc/N)**aN:.2f}")

# ── 예제 3. 학습에 든 계산량 C ≈ 6·N·D ─────────────────────────
print("\n[예제 3] 학습 계산량 (부동소수점 연산 횟수)")
for name, N, D in [("GPT-3", 175e9, 300e9), ("Gopher", 280e9, 300e9), ("Chinchilla", 70e9, 1.4e12)]:
    print(f"  {name:10s} N={N:.3g}, D={D:.3g} → C ≈ {6*N*D:.2e}  (토큰/파라미터 = {D/N:.1f})")

# ── 예제 4. '갑자기'는 채점 방식이 만든 착시일까? ────────────────────
logN = np.linspace(7, 12, 11)                          # 모델 크기 10^7 ~ 10^12
p_token = 1 / (1 + np.exp(-1.6 * (logN - 9.5)))        # 한 토큰 정답률: 매끄럽게 증가
exact5 = p_token ** 5                                  # 다섯 자리 답이 '모두' 맞아야 정답
print("\n[예제 4] 같은 모델, 다른 채점")
print("  log10(N)  토큰 정답률  5자리 완전 일치")
for l, a, b in zip(logN, p_token, exact5):
    print(f"   {l:5.1f}      {a:6.1%}       {b:6.1%}")

json.dump({"sizes": sizes, "losses": [round(x, 4) for x in losses],
           "slope": round(slope, 4), "icpt": round(icpt, 4)}, open("ch07_data.json", "w"))
