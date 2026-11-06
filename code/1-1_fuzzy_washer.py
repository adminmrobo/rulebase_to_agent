# 예제 5 · 퍼지 세탁기: 딱 끊는 규칙 vs 정도로 섞는 규칙 (숫자는 설명용 가정)
def crisp_time(dirt, oil):                 # 1장식 규칙: 50을 넘느냐 아니냐
    many_dirt, much_oil = dirt >= 50, oil >= 50
    return {(False, False): 10, (False, True): 20, (True, False): 25, (True, True): 40}[(many_dirt, much_oil)]

def much(x):                               # 소속 함수: 20 이하면 0, 80 이상이면 1, 그 사이는 비스듬히
    return min(1, max(0, (x - 20) / 60))

def fuzzy_time(dirt, oil):                 # 퍼지 규칙: "많다"를 0~1의 정도로
    many, few = much(dirt), 1 - much(dirt)          # 더러움이 많은 정도, 적은 정도
    oily, clean = much(oil), 1 - much(oil)          # 기름때가 많은 정도, 적은 정도
    rules = [(min(few, clean), 10), (min(few, oily), 20),   # IF 더러움 적고 기름때 적으면 THEN 10분 ...
             (min(many, clean), 25), (min(many, oily), 40)]
    return sum(w * t for w, t in rules) / sum(w for w, _ in rules)   # 규칙들의 가중 평균

print("더러움  기름때 │ 딱 끊는 규칙  퍼지 규칙")
for dirt, oil in [(30, 20), (49, 20), (51, 20), (70, 20), (70, 60), (90, 90)]:
    print(f"  {dirt:3d}    {oil:3d}  │   {crisp_time(dirt, oil):3d}분      {fuzzy_time(dirt, oil):6.2f}분")
