# 2편 1장 부록 — 진짜 API로 돌리는 최소 에이전트 루프
# 필요한 것: pip install anthropic, 환경변수 ANTHROPIC_API_KEY
import anthropic

client = anthropic.Anthropic()          # API 키는 환경변수에서 읽는다 (코드에 적지 않는다)
MODEL = "claude-opus-5-5"               # 쓰는 모델 이름. 문서에서 최신 이름을 확인할 것

# ① 도구 정의: 이름, 설명, 입력 형식(JSON 스키마). 모델은 이 설명만 보고 언제 쓸지 정한다
TOOLS = [{
    "name": "monthly_payment",
    "description": "원리금균등상환 대출의 월 상환액(원)을 계산한다.",
    "input_schema": {
        "type": "object",
        "properties": {
            "amount": {"type": "number", "description": "대출 원금(원)"},
            "annual_rate": {"type": "number", "description": "연이율. 4.8%면 0.048"},
            "months": {"type": "integer", "description": "상환 개월 수"},
        },
        "required": ["amount", "annual_rate", "months"],
    },
}]

# ② 실제 일은 내 코드가 한다. 모델은 "이 도구를 이 값으로 불러 달라"고 요청할 뿐
def monthly_payment(amount, annual_rate, months):
    r = annual_rate / 12
    return round(amount * r * (1 + r) ** months / ((1 + r) ** months - 1))

def run_tool(name, args):
    if name == "monthly_payment":
        return str(monthly_payment(**args))
    return f"알 수 없는 도구: {name}"

# ③ ReAct 루프: 모델 호출 → 도구 요청이면 실행해서 결과를 돌려줌 → 최종 답이 나올 때까지 반복
def agent(question, max_steps=5):                     # 멈춤 조건: 최대 반복 횟수 (2편 3장)
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        resp = client.messages.create(model=MODEL, max_tokens=1024, tools=TOOLS, messages=messages)
        if resp.stop_reason != "tool_use":            # 도구를 더 안 쓰면 최종 답
            return "".join(b.text for b in resp.content if b.type == "text")
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for b in resp.content:
            if b.type == "tool_use":
                out = run_tool(b.name, b.input)
                print(f"  [행동 {step + 1}] {b.name}({b.input}) → {out}")
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": out})
        messages.append({"role": "user", "content": results})  # 관찰을 돌려준다
    return "반복 한도를 넘어 사람에게 넘깁니다."

if __name__ == "__main__":
    print(agent("1억 원을 연 4.8%로 36개월 빌리면 매달 얼마 갚아야 해? 40개월이면 얼마나 줄어?"))
