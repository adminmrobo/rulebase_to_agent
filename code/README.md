# 실험 노트 코드

각 장 "파이썬 실험 노트"에 실린 코드입니다. 이 폴더(`code/`)에서 실행하세요.

```
pip install numpy pandas scikit-learn gensim
python 1-2_machine_learning_examples.py
```

| 파일 | 장 | 비고 |
|---|---|---|
| 1-1_rulebase_examples.py | 1편 1장 | 플로우차트·규칙 폭발 |
| 1-1_maze_graph.py · 1-1_maze_search.py | 1편 1장 | 미로 → 상태공간 그래프, BFS·DFS·다익스트라 (`python 1-1_maze_search.py 19`) |
| 1-1_fuzzy_washer.py | 1편 1장 | 예제 5 퍼지 세탁기 |
| 1-2 ~ 1-9 | 1편 2~9장 | 1-2는 `data/fish.csv` 사용 |
| 1-5, 1-6 | 1편 5·6장 | 먼저 `python prepare_glove.py`로 GloVe를 받아야 함 |
| 2-1_agent_examples.py ~ 2-6_capstone_agent.py | 2편 | 모두 LLM을 흉내 낸 설명용 모의실험 |
| 2-1_real_api_agent.py | 2편 1장 부록 | 실제 Claude API 호출. `pip install anthropic`, 환경변수 `ANTHROPIC_API_KEY` 필요 |

일부 예제는 실행하면 `chXX_data.json`을 만듭니다. 페이지의 도판이 쓰는 데이터와 같은 것입니다.
