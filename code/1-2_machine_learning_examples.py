# 1편 2장 — 머신러닝 : 실행 예제 모음 (fish.csv, 159마리 7종)
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

KO = {"Bream": "도미", "Roach": "로치", "Whitefish": "화이트피시", "Parkki": "파르키",
      "Perch": "농어", "Pike": "강꼬치고기", "Smelt": "빙어"}
fish = pd.read_csv("data/fish.csv")
fish["종"] = fish["Species"].map(KO)

# ── 예제 1. 1장의 손 규칙을 실제 159마리에 돌려 보면? ─────────────
def rule_ch1(L, W):
    if L >= 30:
        return "도미" if W >= 500 else "강꼬치고기"
    return "빙어" if W < 20 else "농어"

pred = [rule_ch1(L, W) for L, W in zip(fish.Length, fish.Weight)]
acc = np.mean(np.array(pred) == fish["종"].values)
print(f"[예제 1] 1장 손 규칙의 정확도: {acc:.1%} ({int(acc*len(fish))}/{len(fish)}마리)")

# ── 예제 2. 도미 vs 빙어 : 로지스틱 회귀를 직접 구현 ──────────────
two = fish[fish.Species.isin(["Bream", "Smelt"])]
X = two[["Length", "Weight"]].values
y = (two.Species == "Bream").astype(float).values          # 도미=1, 빙어=0
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu) / sd                                          # 표준화

w, b, eta = np.zeros(2), 0.0, 0.1
print("\n[예제 2] 경사하강법으로 눈금 맞추기")
for epoch in range(1, 201):
    z = Xs @ w + b
    p = 1 / (1 + np.exp(-z))                                 # 시그모이드
    loss = -np.mean(y*np.log(p+1e-12) + (1-y)*np.log(1-p+1e-12))
    grad_w = Xs.T @ (p - y) / len(y)                         # (ŷ − y)·x
    grad_b = np.mean(p - y)
    w -= eta * grad_w
    b -= eta * grad_b
    if epoch in (1, 10, 50, 200):
        print(f"  {epoch:3d}번째  손실 {loss:.4f}  w={np.round(w,3)}  b={b:.3f}")
print(f"  학습 정확도: {np.mean((p >= .5) == y):.0%}")

# ── 예제 3. 기계가 스스로 쓴 플로우차트 (결정트리) ─────────────────
feats = ["Length", "Weight", "Height", "Width"]
Xtr, Xte, ytr, yte = train_test_split(fish[feats], fish["종"], test_size=0.25,
                                      stratify=fish["종"], random_state=42)
tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(Xtr, ytr)
print("\n[예제 3] 결정트리가 데이터에서 찾은 규칙 (깊이 3)")
print(export_text(tree, feature_names=["길이", "무게", "높이", "두께"], decimals=1))
print(f"  학습 {tree.score(Xtr, ytr):.1%} / 시험 {tree.score(Xte, yte):.1%}")

# ── 예제 4. "모르겠다" 대신 확률로 답하기 ───────────────────────
scaler = StandardScaler().fit(Xtr)
lr = LogisticRegression(C=20, max_iter=2000).fit(scaler.transform(Xtr), ytr)
small = fish[fish.Species == "Bream"].sort_values("Length").iloc[[0]]   # 가장 작은 도미
L, W = small.Length.item(), small.Weight.item()
print(f"\n[예제 4] 데이터 속 가장 작은 도미 (길이 {L}cm, 무게 {W:.0f}g)")
print(f"  1장 손 규칙 → {rule_ch1(L, W)}")
print(f"  결정트리   → {tree.predict(small[feats])[0]}")
proba = lr.predict_proba(scaler.transform(small[feats]))[0]
top = sorted(zip(lr.classes_, proba), key=lambda t: -t[1])[:3]
print("  로지스틱 회귀 → " + ", ".join(f"{k} {v:.0%}" for k, v in top))
print(f"  로지스틱 회귀 시험 정확도: {lr.score(scaler.transform(Xte), yte):.1%}")

# ── 예제 5. 과적합 : 트리를 깊게 할수록? ─────────────────────────
print("\n[예제 5] 트리 깊이별 정확도")
for d in [1, 2, 3, 5, 8, None]:
    t = DecisionTreeClassifier(max_depth=d, random_state=42).fit(Xtr, ytr)
    print(f"  깊이 {str(d):>4s}: 학습 {t.score(Xtr, ytr):6.1%}  시험 {t.score(Xte, yte):6.1%}")
