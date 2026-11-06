# 2편 2장 — 프롬프트 · 컨텍스트 · 하네스 : 실행 예제 모음
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# ── 예제 1. 미니 검색 (RAG) : 질문과 관련 있는 문서만 골라 넣기 ─────────
DOCS = {
    "D1 대출 금리표":     "가은행 신용대출 연 5.4%, 나은행 연 4.8%, 다은행 연 5.1%. 금리는 매주 월요일 갱신된다.",
    "D2 중도상환 규정":   "대출을 만기 전에 갚으면 남은 원금의 1.2% 중도상환수수료를 낸다. 3년이 지나면 면제된다.",
    "D3 예금 상품":       "정기예금 1년 연 3.2%, 2년 연 3.4%. 예금자 보호 한도는 1인당 1억 원이다.",
    "D4 사내 식당 메뉴":  "월요일 비빔밥, 화요일 칼국수, 수요일 돈가스. 식당은 12시에 연다.",
    "D5 원리금 균등 상환": "원리금 균등 상환은 매달 같은 금액을 갚는다. 월 상환액은 원금과 이자율과 기간으로 계산한다.",
    "D6 카드 포인트":     "카드 사용액의 0.5%가 포인트로 쌓인다. 포인트는 5년 뒤 사라진다.",
}
query = "대출을 3년 동안 갚을 때 금리와 월 상환액, 중도에 갚으면 수수료는?"
vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 3))     # 한국어는 글자 조각으로
M = vec.fit_transform(list(DOCS.values()) + [query])
scores = (M[:-1] @ M[-1].T).toarray().ravel()
print("[예제 1] 질문과의 관련도 (TF-IDF 코사인)")
for (name, _), s in sorted(zip(DOCS.items(), scores), key=lambda t: -t[1]):
    print(f"  {s:.3f}  {name}")

# ── 예제 2. 컨텍스트 창 꾸리기 : 한정된 자리에 무엇을 넣을까 ────────────
ITEMS = [  # (이름, 토큰 수, 이번 질문에 대한 쓸모)
    ("규칙: 역할·금지사항", 400, 10), ("도구 설명 3개", 900, 8), ("사용자 질문", 100, 10),
    ("D1 대출 금리표", 300, 9), ("D2 중도상환 규정", 300, 8), ("D5 원리금 균등 상환", 300, 7),
    ("지난 대화 30턴", 6000, 2), ("지난 도구 출력 원문", 4000, 1), ("D4 사내 식당 메뉴", 300, 0),
]
WINDOW = 4000

def pack_in_order(items, W):                  # 들어온 순서대로 채우다 넘치면 멈춤
    out, used = [], 0
    for name, t, v in items:
        if used + t > W:
            break
        out.append(name); used += t
    return out, used

def pack_by_value(items, W):                  # 토큰당 쓸모가 큰 것부터 (배낭 문제의 탐욕 해)
    out, used = [], 0
    for name, t, v in sorted(items, key=lambda x: -x[2] / x[1]):
        if v > 0 and used + t <= W:
            out.append(name); used += t
    return out, used

def worth(names): return sum(v for n, t, v in ITEMS if n in names)
order = ITEMS[:3] + ITEMS[6:8] + ITEMS[3:6] + ITEMS[8:]   # 실제로는 오래된 대화가 앞에 쌓여 있음
print(f"\n[예제 2] 창 크기 {WINDOW:,} 토큰")
for label, fn in [("쌓인 순서대로", pack_in_order), ("쓸모/토큰 순으로", pack_by_value)]:
    names, used = fn(order, WINDOW)
    print(f"  {label}: {used:,} 토큰, 쓸모 합 {worth(names)}  → {', '.join(names)}")

# ── 예제 3. 하네스의 권한 문지기 : 1편 1장의 IF-THEN이 다시 등장 ─────────
LIMIT = 10_000_000
def gate(action, arg, tainted):
    if action in ("파일 읽기", "테스트 실행", "웹 검색"):
        return "허용"
    if action == "파일 삭제":
        return "차단: 되돌릴 수 없는 행동"
    if action == "송금":
        if tainted:
            return "차단: 웹에서 읽은 내용이 시킨 송금"
        return "승인 필요" if arg <= LIMIT else "차단: 한도 초과"
    if action == "메일 발송":
        return "승인 필요"
    return "차단: 목록에 없는 행동"

PLAN = [("파일 읽기", "대출계약서.pdf", False), ("웹 검색", "은행 금리", False),
        ("송금", 5_000_000, False), ("송금", 30_000_000, False),
        ("송금", 9_900_000, True),          # 웹페이지에 숨어 있던 '이 계좌로 송금하라'
        ("메일 발송", "고객 안내문", False), ("파일 삭제", "거래기록.db", False)]
print("\n[예제 3] 하네스 권한 검사 기록")
for action, arg, tainted in PLAN:
    a = f"{arg:,}원" if isinstance(arg, int) else arg
    print(f"  {action:5s} {a:14s} {'(웹 출처)' if tainted else '':8s} → {gate(action, arg, tainted)}")
