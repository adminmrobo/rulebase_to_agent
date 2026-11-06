# 1편 1장 — 플로우차트와 rule base : 실행 예제 모음
from collections import deque

# ── 예제 1. if-else 규칙으로 물고기 분류하기 ──────────────────
def classify_fish(length_cm, weight_g):
    if length_cm >= 30:
        if weight_g >= 500:
            return "도미"
        return "강꼬치고기"
    if weight_g < 20:
        return "빙어"
    return "농어"

print("[예제 1] 규칙 기반 물고기 분류")
for name, L, W in [("도미 샘플", 35, 700), ("빙어 샘플", 12, 15),
                   ("아기 도미", 22, 250)]:          # 규칙이 예상 못한 경우
    print(f"  {name:6s} 길이 {L}cm, 무게 {W}g → {classify_fish(L, W)}")
print("  → '아기 도미'는 규칙에 없는 경우라 농어로 잘못 분류됩니다.\n")

# ── 예제 2. 전방 추론(forward chaining) 미니 추론 엔진 ──────────
RULES = [
    ({"비늘이 있다", "아가미가 있다"}, "물고기다"),
    ({"물고기다", "몸이 붉다", "이마가 둥글다"}, "도미다"),
    ({"물고기다", "몸이 은빛이다", "크기가 작다"}, "빙어다"),
    ({"도미다"}, "회로 먹는다"),
]

def forward_chain(facts, rules):
    facts = set(facts)
    changed = True
    step = 0
    while changed:
        changed = False
        for cond, concl in rules:
            if cond <= facts and concl not in facts:
                step += 1
                print(f"  {step}단계: {' ∧ '.join(sorted(cond))} → {concl}")
                facts.add(concl)
                changed = True
    return facts

print("[예제 2] 전방 추론 엔진")
result = forward_chain({"비늘이 있다", "아가미가 있다", "몸이 붉다", "이마가 둥글다"}, RULES)
print("  최종 사실:", sorted(result), "\n")

# ── 예제 3. 상태공간 미로 탐색 (BFS, 오픈·클로즈드 리스트) ─────
GRAPH = {
    "S1": ["S2"],
    "S2": ["S1", "S3", "S4", "S5"],
    "S3": ["S2"],
    "S4": ["S2", "S6"],
    "S5": ["S2"],
    "S6": ["S4"],          # 출구
}

def bfs(start, goal):
    open_list = deque([[start]])   # 아직 탐색하지 않은 후보 (경로째 저장)
    closed = set()                 # 탐색을 마친 상태
    while open_list:
        path = open_list.popleft()
        node = path[-1]
        if node in closed:
            continue
        print(f"  방문 {node:3s} | 오픈 {[p[-1] for p in open_list]} | 클로즈드 {sorted(closed)}")
        if node == goal:
            return path
        closed.add(node)
        for nxt in GRAPH[node]:
            if nxt not in closed:
                open_list.append(path + [nxt])
    return None

print("[예제 3] 너비우선 탐색")
print("  최단 경로:", " → ".join(bfs("S1", "S6")), "\n")

# ── 예제 4. 규칙 폭발 : 조건이 늘면 경우의 수는? ──────────────
print("[예제 4] 예/아니오 조건 n개가 만드는 경우의 수 2^n")
for n in [5, 10, 20, 30, 40]:
    print(f"  조건 {n:2d}개 → {2**n:,}가지")

# ── 예제 5. 규칙 + 문장 틀로 쓰는 시황 기사 봇 (예시 숫자) ─────
def market_brief(index, change, foreign_net):
    trend = "상승세" if change > 0 else "하락세" if change < 0 else "보합세"
    if foreign_net > 0:
        cause = f"외국인이 {foreign_net:,}억 원어치를 순매수하면서"
    elif foreign_net < 0:
        cause = f"외국인이 {-foreign_net:,}억 원어치를 순매도하면서"
    else:
        cause = "뚜렷한 매매 주체 없이"
    return f"{cause} 지수가 {index:,.2f}({change:+.2f}%)로 {trend}를 보이고 있다."

print("\n[예제 5] 규칙 기반 시황 문장 생성 (가상의 숫자)")
print("  " + market_brief(2580.15, 0.85, 1453))
print("  " + market_brief(2541.30, -0.62, -820))
