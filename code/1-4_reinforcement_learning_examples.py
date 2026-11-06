# 1편 4장 — 강화학습 : 실행 예제 모음
import numpy as np

# 5×5 미로. S 출발, G 출구(+10), # 벽, 한 걸음마다 −1
MAZE = ["S...#",
        ".##.#",
        "...#.",
        ".#...",
        "...#G"]
H, W = len(MAZE), len(MAZE[0])
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]          # 위, 아래, 왼쪽, 오른쪽
ARROW = "↑↓←→"

def step(state, a, grid=MAZE, rewards=None):
    r, c = state
    nr, nc = r + ACTIONS[a][0], c + ACTIONS[a][1]
    if not (0 <= nr < H and 0 <= nc < W) or grid[nr][nc] == "#":
        nr, nc = r, c                                  # 벽에 부딪히면 제자리
    cell = grid[nr][nc]
    if rewards and cell in rewards:
        return (nr, nc), rewards[cell], True
    if cell == "G":
        return (nr, nc), 10.0, True
    return (nr, nc), -1.0, False

def q_learning(episodes, eps=0.1, alpha=0.5, gamma=0.95, seed=0, grid=MAZE, rewards=None):
    rng = np.random.default_rng(seed)
    Q = np.zeros((H, W, 4))
    log = []
    for ep in range(episodes):
        s, total, n = (0, 0), 0.0, 0
        for n in range(1, 101):
            if rng.random() < eps:
                a = int(rng.integers(4))                  # 탐험: 아무 방향
            else:
                a = int(np.argmax(Q[s]))                  # 활용: 지금까지 가장 좋았던 방향
            s2, r, done = step(s, a, grid, rewards)
            target = r if done else r + gamma * Q[s2].max()
            Q[s][a] += alpha * (target - Q[s][a])         # Q-러닝 갱신식
            s, total = s2, total + r
            if done:
                break
        log.append((n, total))
    return Q, log

# ── 예제 1. 지도 없이 미로 출구 찾기 ─────────────────────────
Q, log = q_learning(200)
print("[예제 1] Q-러닝 미로 (에피소드별 걸음 수와 총보상)")
for ep in [1, 5, 20, 50, 200]:
    n, total = log[ep - 1]
    print(f"  {ep:3d}번째 시도: {n:3d}걸음, 총보상 {total:6.1f}")

print("\n  학습된 행동 지도 (각 칸에서 고르는 방향)")
for r in range(H):
    row = ""
    for c in range(W):
        ch = MAZE[r][c]
        row += f" {ch} " if ch in "#G" else f" {ARROW[int(np.argmax(Q[r, c]))]} "
    print("  " + row)

# ── 예제 2. 탐험 vs 활용 : 가까운 동전(+3)과 먼 보물(+20) ────────
TREASURE = ["S.C..",
            ".....",
            ".###.",
            ".....",
            "....T"]
REW = {"C": 3.0, "T": 20.0}

def greedy_run(Q):                      # 학습이 끝난 뒤, 탐험 없이 한 번 실행
    s, total = (0, 0), 0.0
    for _ in range(50):
        s, r, done = step(s, int(np.argmax(Q[s])), TREASURE, REW)
        total += r
        if done:
            break
    return total

print("\n[예제 2] 학습 중 탐험률 ε 에 따른 최종 성적 (30번 반복)")
for eps in [0.0, 0.2, 0.5, 0.8]:
    res = [greedy_run(q_learning(500, eps=eps, seed=sd, grid=TREASURE, rewards=REW)[0])
           for sd in range(30)]
    found = sum(r > 5 for r in res)
    print(f"  ε = {eps:.1f} : 평균 총보상 {np.mean(res):5.1f}, 보물 발견 {found:2d}/30")
