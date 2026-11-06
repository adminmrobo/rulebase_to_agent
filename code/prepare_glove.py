# 1-5, 1-6 실험에 쓰는 GloVe 단어 벡터(50차원, 40만 단어)를 내려받아 data/glove50.kv로 저장한다.
# 필요한 것: pip install gensim  (처음 한 번, 약 70MB 내려받음)
import gensim.downloader as api
kv = api.load("glove-wiki-gigaword-50")
kv.save("data/glove50.kv")
print("저장 완료: data/glove50.kv", len(kv.key_to_index), "단어")
