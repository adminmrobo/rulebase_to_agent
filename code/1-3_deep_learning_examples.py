# 1편 3장 — 딥러닝 : 실행 예제 모음
import json
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

X4 = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)

# ── 예제 1. 퍼셉트론 하나로 AND와 XOR 배우기 ───────────────────
def perceptron(X, y, epochs=50, eta=0.1):
    w, b = np.zeros(2), 0.0
    for _ in range(epochs):
        for xi, yi in zip(X, y):
            y_hat = 1 if xi @ w + b > 0 else 0
            w += eta * (yi - y_hat) * xi          # η(y − ŷ)x : 2장의 그 식
            b += eta * (yi - y_hat)
    return [1 if xi @ w + b > 0 else 0 for xi in X]

print("[예제 1] 퍼셉트론 하나")
for name, y in [("AND", [0, 0, 0, 1]), ("XOR", [0, 1, 1, 0])]:
    pred = perceptron(X4, np.array(y))
    print(f"  {name}: 정답 {y} / 예측 {pred} → {sum(p == t for p, t in zip(pred, y))}/4 맞음")

# ── 예제 2. 은닉층 하나를 넣고 역전파로 XOR 풀기 ─────────────────
rng = np.random.default_rng(0)
y = np.array([[0], [1], [1], [0]], dtype=float)
W1, b1 = rng.normal(0, 1, (2, 2)), np.zeros(2)       # 입력 2 → 은닉 2
W2, b2 = rng.normal(0, 1, (2, 1)), np.zeros(1)       # 은닉 2 → 출력 1
sig = lambda z: 1 / (1 + np.exp(-z))
eta = 1.0
print("\n[예제 2] 2층 신경망 + 역전파")
for epoch in range(1, 5001):
    h = sig(X4 @ W1 + b1)                    # 순전파: 은닉층
    out = sig(h @ W2 + b2)                   #         출력층
    loss = np.mean((out - y) ** 2)
    d_out = (out - y) * out * (1 - out)      # 역전파: 출력층 오차
    d_h = (d_out @ W2.T) * h * (1 - h)       #         은닉층으로 거슬러 전달 (연쇄법칙)
    W2 -= eta * h.T @ d_out;  b2 -= eta * d_out.sum(0)
    W1 -= eta * X4.T @ d_h;   b1 -= eta * d_h.sum(0)
    if epoch in (1, 500, 2000, 5000):
        print(f"  {epoch:4d}번째  손실 {loss:.4f}  출력 {np.round(out.ravel(), 2)}")
print("  최종 판정:", (out.ravel() > .5).astype(int).tolist(), "(정답 [0, 1, 1, 0])")

# 페이지용: 학습된 신경망의 판정 영역 (25x25 격자)
grid = np.linspace(-0.25, 1.25, 25)
region = [[float(sig(sig(np.array([gx, gy]) @ W1 + b1) @ W2 + b2)[0]) for gx in grid] for gy in grid]

# ── 예제 3. 손글씨 숫자 : 픽셀만 주고 배우게 하기 ────────────────
digits = load_digits()                                # 8×8 흑백, 1,797장
Xtr, Xte, ytr, yte = train_test_split(digits.data / 16, digits.target,
                                      test_size=0.25, random_state=0, stratify=digits.target)
print(f"\n[예제 3] 손글씨 숫자 {len(digits.data):,}장, 픽셀 {digits.data.shape[1]}개")
lr = LogisticRegression(max_iter=3000).fit(Xtr, ytr)
mlp = MLPClassifier(hidden_layer_sizes=(16,), max_iter=3000, random_state=0).fit(Xtr, ytr)
mlp2 = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=3000, random_state=0).fit(Xtr, ytr)
n_params = lambda m: sum(w.size for w in m.coefs_) + sum(b.size for b in m.intercepts_)
print(f"  로지스틱 회귀(층 없음)     시험 정확도 {lr.score(Xte, yte):.1%}")
print(f"  신경망 은닉층 16           시험 정확도 {mlp.score(Xte, yte):.1%}  (가중치 {n_params(mlp):,}개)")
print(f"  신경망 은닉층 64 → 32      시험 정확도 {mlp2.score(Xte, yte):.1%}  (가중치 {n_params(mlp2):,}개)")

# 페이지용: 첫 층 16개 뉴런이 스스로 만든 "특징 필터" 8개, 숫자 샘플 4개
filters = [mlp.coefs_[0][:, i].reshape(8, 8).round(3).tolist() for i in range(8)]
samples = [(digits.images[i] / 16).round(2).tolist() for i in [0, 1, 2, 3]]
json.dump({"region": region, "filters": filters, "samples": samples},
          open("ch03_data.json", "w"))
