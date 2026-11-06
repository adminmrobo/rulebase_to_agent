# 플로우 차트의 rule base에서 일하는 AI까지 — 표지 프롬프트 모음 (17장)

Genspark에 한 장씩 붙여 넣으면 됩니다. 매번 **참고 이미지 4장**(`doc_e13`, `asst_e13`, `fly_e13`, 주판봇 `images/jupanbot/E13_neutral.png` — adminmrobo/fruitfly-lab-expressions, 커밋 5269662, 2026-11-05 새 픽셀 그림)을 함께 올립니다.

| 순서 | 묶음 | 비율 · 크기 | 저장할 파일 이름 |
|---|---|---|---|
| A1 | 시리즈 표지 (목차 첫 화면) | 16:9 · 가로 1920 이상 | `cover_index.png` |
| A2 | 저장소 미리보기 (GitHub Social preview) | 2:1 · 1280×640 | `social_preview.png` |
| B1~B9 | 1편 각 장 첫 화면 표지 | 16:9 · 가로 1920 이상 | `cover_1-1.png` ~ `cover_1-9.png` |
| B10~B15 | 2편 각 장 첫 화면 표지 | 16:9 · 가로 1920 이상 | `cover_2-1.png` ~ `cover_2-6.png` |

**받은 뒤 확인:** 비율 맞음 · 그림 안에 글자 없음 · 네 캐릭터 외형이 참고 그림과 같음 · 주판봇이 무한궤도로 바닥에 서 있고 키가 박사의 약 3/4 · **위쪽 가운데가 어둡게 비어 있음**(장 제목이 그 자리에 올라갑니다). 파일 이름을 위 표대로 붙여 한 zip으로 주시면 15개 장에 한 번에 넣습니다.

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**주판봇이 옛 모습(흰 둥근 머리·노란 눈)으로 나오면:** `Same scene. Redraw only the robot to match the attached E13_neutral reference exactly: beige CRT-monitor head, dark green screen with mint pixel face, thin antenna with one red-brown abacus bead, gray segmented arms with mitten hands, two dark gray tank treads on the floor. Still no text.`

**제목 자리가 막히면:** `Same scene. Push everything down a little and keep the upper middle third as a dark empty lab wall. Still no text.`

> 이 시리즈 페이지는 표지 위에 장 제목을 직접 얹습니다. 그래서 다른 시리즈와 달리 왼쪽 아래 대신 **위쪽 가운데**를 비워 둡니다. 휴대폰에서는 제목이 그림 아래로 내려가므로 그림이 가려지지 않습니다.

---
## A. 시리즈 표지 — 목차와 저장소 미리보기 (2장)

### A1. 시리즈 표지 · 목차(index) 첫 화면 → `cover_index.png`

```
웹페이지 목차 첫 화면 맨 위에 거는 시리즈 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 시리즈 전체(태엽 기계 → 학습 → 언어 모델 → 추론 → 일하는 에이전트)를 한 장에: 왼쪽 끝 호박색 종이 플로우차트 벽에서 시작해 오른쪽 끝 여러 모니터가 이어진 작업 책상까지 이어지는 긴 연구실 복도, 바닥에 빛나는 한 줄기 실이 이어진다
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (시리즈 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration for a series index page, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: one long night-lab corridor read from left to right as a journey. At the far left, a wall covered with a glowing amber paper flowchart of diamond decision boxes beside old 1980s terminals; in the middle, a brass balance scale, a small neural-network lattice of glowing beads, and floating word-cards connected by thin light lines; at the far right, a modern desk with several connected monitors where small helper robots-of-light pass task cards to each other. A single glowing teal thread runs along the floor from the flowchart on the left to the desk on the right, tying all stations together.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, in the center left walking forward holding an old flowchart card in one hand and pointing right toward the desk, proud;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the center right with a clipboard of blank checklists, looking back at the scientist, excited;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, at the left near the flowchart wall facing right, studying the glowing thread with a magnifying glass, curious;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, at the right in front of the monitors facing left, rolling forward on its treads and waving one mitten hand, confident.
Visual metaphor of the topic: from hand-written rules to an AI that learns, reasons and then works on its own, all connected by one thread.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, warm, the start of a long journey.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### A2. 저장소 미리보기 · GitHub Social preview → `social_preview.png`

```
GitHub 저장소 미리보기(Social preview)용 그림 1장을 만들어 줘.
- 비율 2:1, 1280×640px (최소 640×320)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 링크 카드에서 가장자리가 잘리므로 캐릭터·핵심 소품은 가운데(가로 15~85%, 세로 15~85%) 안에
- 왼쪽에는 호박색 플로우차트 카드, 오른쪽에는 빛나는 작업 모니터, 그 사이를 청록색 실 한 줄이 잇는다
아래 영어 프롬프트를 그대로 써 줘.

Social preview banner illustration, wide 2:1, 1280×640 pixels.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness, simple dark background.
Scene: on the left a single large glowing amber paper flowchart card with diamond boxes pinned to a dark wall; on the right a glowing modern monitor showing a simple blank task board; one glowing teal thread runs from the flowchart card to the monitor across the middle.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, in the center left holding one end of the thread, proud;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the center right holding the thread up so it does not tangle, cheerful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, at the left by the flowchart card facing right, pointing at the start of the thread, curious;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, at the right in front of the monitor facing left, holding the other end of the thread in one mitten hand, confident.
Composition: keep all four characters and key props inside the central safe area (15% to 85% of the width and height), large and readable even as a small thumbnail; keep the background simple with few small details.
Mood: friendly, inviting, clear at small size.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

---
## B. 각 장 표지 — 16:9 (가로 1920 이상)

### B1. 1편 1장 · 태엽 기계: 플로우차트와 rule base → `cover_1-1.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 뒷벽 전체에 빛나는 호박색 종이 플로우차트. 왼쪽은 마름모 몇 개로 단정하지만 오른쪽으로 갈수록 가지가 불어나 엉킨 그물이 된다
- 아래에는 1980년대 단말기 두 대와 규칙 카드가 넘쳐 쏟아지는 회색 서류함들
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, the back wall is covered with a huge glowing amber paper flowchart made of diamond-shaped decision boxes and arrows; on the left it is neat with only a few diamonds, toward the right the branches multiply until they tangle into an overwhelming web. Below it stand two old 1980s computer terminals with green screens and gray filing cabinets overflowing with blank rule cards that spill onto the floor.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pinning one more blank diamond card onto the wall, proud;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding a tall wobbling stack of blank rule cards, worried;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, tracing a tangled branch with a magnifying glass, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, pulling a long blank printout scroll out of a terminal, confident.
Visual metaphor of the topic: hand-written rules that work while the world is small and explode as it grows.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B2. 1편 2장 · 눈금을 스스로 맞추는 저울: 머신러닝 → `cover_1-2.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 연구실이 작은 밤 생선 가게로: 얼음 위 여러 종류의 생선, 황동 저울, 숫자 없는 자
- 공중에 빛 점들이 두 무리로 떠 있고 그 사이로 금빛 선 하나가 스스로 그어진다
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, the lab is turned into a small night fish stall: several kinds of fish lie on crushed ice beside a glowing brass balance scale and a long wooden ruler with tick lines but no numbers. Above the counter, soft glowing dots float in the air like a scatter plot in two clusters, and a thin golden line slowly draws itself between the clusters, as if the data were drawing its own boundary.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the golden line with a delighted face;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center writing on a blank clipboard, focused;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, measuring the length of a fish with the ruler, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, holding up a fish in one mitten and a small wooden abacus in the other, confident.
Visual metaphor of the topic: the machine adjusts its own scale from data instead of a hand-written threshold.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B3. 1편 3장 · 보는 법 자체를 배우는 기계: 딥러닝 → `cover_1-3.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 뒤쪽에 빛나는 신경망 층(점과 금빛 실로 된 세로 패널) 여러 장
- 왼쪽의 치와와 얼굴·블루베리 머핀 사진 카드가 층을 지나며 선과 모양 무늬로 바뀌고, 오른쪽에서 치와와 더미와 머핀 더미로 나뉘어 나온다
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, a row of tall glowing neural network panels made of luminous dots connected by fine golden threads rises in the background. On the left, small photo cards of chihuahua faces and blueberry muffins float into the first panel; deeper in, they turn into simple glowing edge and blob patterns, and on the right they come out sorted into two neat stacks, one of chihuahuas and one of muffins.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center with purple sparks between both hands, explaining;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding a blueberry muffin and squinting at it, puzzled;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, comparing a chihuahua card and a muffin card side by side, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, catching the sorted cards into two baskets, confident.
Visual metaphor of the topic: the machine learns which features to look at, layer by layer.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B4. 1편 4장 · 당근과 채찍의 훈련소: 강화학습 → `cover_1-4.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 바닥에 커다란 미로 판, 칸마다 청록 화살표가 켜져 있다
- 가까운 곳에 빛나는 주판알 한 줌, 먼 곳에 보물 상자, 벽에 초록·빨강 불빛만 있는 점수판(숫자 없음), 책상 위 바둑판
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, a large maze board covers the floor of the night lab, and on many tiles a small teal arrow glows showing the learned direction. A handful of glowing abacus beads lies close to the start as a small reward, a treasure chest glows far away at the end, a scoreboard on the wall shows only green and red lights without numbers, and a Go board with black and white stones sits on a side desk.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center holding a carrot in one hand and a soft foam stick in the other, smiling;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center marking arrows on a blank map sheet, focused;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, stepping onto an unexplored tile on purpose, curious;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, standing on its treads inside the maze next to the nearby beads, tempted.
Visual metaphor of the topic: learning from rewards and penalties, and the choice between a sure small prize and exploring for a big one.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B5. 1편 5장 · 말을 숫자로 바꾸다: 단어 벡터 → `cover_1-5.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 연구실 천장이 밤하늘 지도처럼: 그림 카드(왕관·남자·여자·강·은행 건물·물고기 등, 글자 없음)가 별자리처럼 떠 있고 비슷한 것끼리 가까이 모여 있다
- 왕관 카드에서 다른 카드로 이어지는 화살표 몇 개, 작업대 위 긴 리본이 가위로 조각조각 잘리는 중
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, the lab ceiling glows like a star map: small picture cards with simple icons and no letters — a crown, a man, a woman, a river, a bank building, a fish, an apple — float like constellations, and similar cards gather close together. A few glowing arrows connect the crown card to other cards like vector arithmetic. On the workbench a long paper ribbon is being cut into small pieces by scissors.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center drawing a glowing arrow between two cards in the air;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding an apple and looking at the apple card, curious;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, cutting the ribbon into pieces with scissors, focused;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, sliding cards on an abacus frame as if measuring distances, confident.
Visual metaphor of the topic: words become points on a map where meaning is distance.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B6. 1편 6장 · 한눈에 모든 단어를 보는 눈: 트랜스포머 → `cover_1-6.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 작업대 위 빈 카드 한 줄(문장). 카드끼리 굵기가 다른 빛나는 실로 이어져 있다
- 가운데 카드 하나는 강 그림과 은행 건물 그림이 반반, 강 쪽 카드에서 오는 실이 가장 굵다. 위에서 여러 개의 스포트라이트
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, a row of blank cards stands on the workbench like a sentence, and every card is connected to every other card by glowing threads of different thickness. One card in the middle shows half a river icon and half a bank building icon; the thickest threads come from the river-side cards and pull it toward the river half. Several small spotlights shine down from above, each lighting a different card.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center adjusting a spotlight, explaining;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding the half-river half-bank card, tilting her head;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, plucking one thin thread like a string, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, gathering many threads in both mittens at once, confident.
Visual metaphor of the topic: every word looks at every other word at the same time and decides whom to listen to.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B7. 1편 7장 · "갑자기"의 정체: 스케일링 → `cover_1-7.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 왼쪽에서 오른쪽으로 점점 커지는 빛나는 기계 상자 다섯 개가 계단처럼 늘어서 있다
- 옆에 책 더미가 점점 높아지고, 벽에는 숫자 없는 매끈한 곡선 그래프, 커다란 바늘 계량기
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, five glowing machine boxes stand in a row like stairs, each larger than the one before, from small on the left to huge on the right. Beside them, stacks of books grow taller in the same way. On the wall, a smooth rising curve is drawn on a grid without any numbers, and a big analog gauge with a needle points high.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the smooth curve with a baton;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center carrying an armful of books toward the biggest box;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, measuring the step between two boxes with a tape, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, flicking abacus beads as if adding up a huge sum, sparkling eyes.
Visual metaphor of the topic: nothing appeared suddenly — size, data and compute grew step by step along a predictable curve.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B8. 1편 8장 · ChatGPT의 순간: 사람의 선호로 길들이기 → `cover_1-8.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 가운데 심사대 위에 빈 답안 카드 두 장, 사람들이 한쪽에 별 스티커를 붙이고 있다
- 커다란 학습 기계에 고삐 끈이 매여 박사가 살짝 당기고 있다. 구석에는 거울 앞에서 박수 치는 작은 앵무새 장난감(아첨)
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, on a judging desk in the center two blank answer cards stand side by side, and small star stickers are being placed on one of them. A large glowing learning machine on the right is tied with a soft rein that the scientist holds gently so it does not run too far. In a corner, a small toy parrot claps in front of a mirror.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center holding the rein lightly, calm;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center placing a star sticker on one card, thoughtful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, pointing at the toy parrot with a raised eyebrow, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, holding up a card covered with star stickers and blushing, proud.
Visual metaphor of the topic: teaching a model what people prefer, with a rein so it does not chase praise too far.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B9. 1편 9장 · 생각하는 시간을 사다: 추론 모델 → `cover_1-9.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 작업대에 길게 풀린 연습장 두루마리, 글자 대신 선과 점으로 된 풀이 낙서와 되돌아간 화살표
- 여러 갈래의 빛나는 길이 한 정답 깃발로 모이고, 옆에 체크 표시 도장(규칙 채점)과 모래시계
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, a long scroll of scratch paper unrolls across the workbench, filled with doodle-like working steps made of lines, dots and arrows that sometimes loop back to an earlier step, with no letters or numbers. Above it, several glowing paths branch out and most of them meet at one small flag. Beside the scroll sit a big check-mark stamp and an hourglass.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center turning the hourglass over, thoughtful;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center following one glowing path with her finger, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, pressing the check-mark stamp onto the scroll, firm;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, carefully re-checking with a small wooden abacus, focused.
Visual metaphor of the topic: spending more time thinking, trying several paths and checking the answer by rules.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B10. 2편 1장 · 에이전트 모델: 행동을 배운 AI → `cover_2-1.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 작업대 위 원형 트랙에 세 정거장: 전구 표지(생각) → 렌치 표지(행동) → 눈 표지(관찰)
- 주판봇이 도구 벨트를 차고 있고, 벽에는 문·서랍·계산기 같은 도구 아이콘 판
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, a small circular track on the workbench passes three glowing stations marked only by icons — a light bulb, a wrench and an eye — and a small cart travels around it. On the wall hangs a pegboard of tools: a door key, a drawer handle, a calculator, a magnifying glass, a small laptop with a blank screen.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the light-bulb station, explaining;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center handing a wrench to the robot, encouraging;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, watching the eye station with arms crossed, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, wearing a tool belt and reaching for the key on the pegboard, eager.
Visual metaphor of the topic: an AI that does not just answer but thinks, acts with tools and looks at the result.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B11. 2편 2장 · 프롬프트 → 컨텍스트 → 하네스 → `cover_2-2.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 가운데에 세 겹 상자: 쪽지 한 장(프롬프트) → 카드가 펼쳐진 작은 책상(컨텍스트) → 그 둘을 감싼 유리 작업실(하네스)
- 작업실 문 앞에 마름모 모양 회전문(문지기), 잠긴 도구함
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, in the center stands a set of nested frames: a single small note on top, around it a small desk with a limited number of cards laid out, and around both a glass workroom with tool racks, a locked toolbox and a door. In front of the door stands a diamond-shaped turnstile gate with a green and a red lamp, letting only some carts through.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center sketching the nested frames in the air;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center choosing which cards to place on the small desk, careful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, holding a suspicious card with a hidden note behind it, alert;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, inside the glass workroom, waiting at the turnstile with a cart, patient.
Visual metaphor of the topic: the same model works differently depending on what it sees and the environment around it.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B12. 2편 3장 · 루프 엔지니어링: 언제 반복하고 언제 멈추나 → `cover_2-3.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 작업대 위 고리 모양 컨베이어가 계속 돈다. 한쪽에 초록·빨강 등이 달린 검사 문(검증기)
- 옆에 모래시계, 빨간 팔각형 멈춤 표지(글자 없음), 동전 대신 주판알이 줄어드는 예산 그릇
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, a looping conveyor belt runs in a circle on the workbench, carrying small boxes around again and again. On one side of the loop stands an inspection gate with a green and a red lamp that checks each box. Beside it sit an hourglass, a red octagonal stop sign with no text, and a bowl of abacus beads that slowly empties as a budget.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center holding a timer and watching the loop;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center writing a small note and slipping it onto a box for the next round;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, operating the inspection gate with a firm hand on its lever;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, waving happily as if saying it is done while the red lamp is on, sheepish.
Visual metaphor of the topic: repeat until a checker says it is done, and stop when time, budget or progress runs out.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B13. 2편 4장 · 오케스트레이션: 지휘자 에이전트와 서브에이전트 → `cover_2-4.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 박사가 지휘대에서 지휘봉을 들고, 나머지 셋이 각자 다른 일을 '연주'한다
- 보면대 위 악보는 음표만(글자·숫자 없음), 뒤쪽에 작업 카드가 세 갈래로 나뉘었다가 다시 한 바구니로 모인다
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, the scientist stands on a small conductor's podium in the center, and the other three each play a different part like an orchestra. Music stands hold sheets with only simple notes and no letters or numbers. Behind them, a stream of task cards splits into three lanes and joins again into one basket.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, on the podium at the back center conducting with a baton, energetic;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center reading through a pile of document cards like playing a part;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, checking cards with a magnifying glass as they return;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, flicking a small wooden abacus like an instrument, confident.
Visual metaphor of the topic: one lead agent splits the work, several sub-agents play their parts, and the results come back together.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B14. 2편 5장 · 헤르메스로 본 자가개선 루프 → `cover_2-5.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 오른쪽 벽 전체가 커다란 황동 카드 서랍장. 몇 칸은 청록색으로 빛나고 한 칸은 붉은 경고등
- 왼쪽 책상 위 돋보기 검사대 아래 빛나는 매뉴얼 카드, 쌓인 카드 묶음
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, in an archive corner, the right wall is a huge brass card-catalog cabinet with many small drawers; some drawers glow teal and one drawer has a red warning lamp above it and is pulled half open. On a desk on the left, a magnifying-glass inspection stand shines light down on a glowing manual card, next to a neat stack of cards.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center sliding a teal-glowing drawer shut, satisfied;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center sorting manual cards into two piles, careful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, inspecting a card under the magnifying-glass stand, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, holding up a glowing manual card it just wrote, proud.
Visual metaphor of the topic: saving only the procedures that passed a check, so the agent gets better with use.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B15. 2편 6장 · 강화학습이 꿰는 실 → `cover_2-6.png`

```
웹페이지 첫 화면 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (종이·카드·화면은 빈칸이나 그림으로만)
- 화면을 가로지르는 금빛 실 한 가닥이 작은 소품들을 차례로 꿴다: 플로우차트 종이, 생선과 저울, 신경망, 미로 속 로봇, 단어 카드, 빛 실 그물, 말풍선, 렌치 쥔 손, 둥근 화살표, 지휘봉, 카드 서랍
- 오른쪽 끝에서 실이 커다란 마름모 모양의 빛나는 문으로 이어진다
- 위쪽 가운데(가로 25~75%, 세로 위 30%)는 어두운 빈 벽으로 비워 둘 것 (장 제목이 올라감). 네 캐릭터의 얼굴과 손은 세로 35~85% 띠 안에
아래 영어 프롬프트를 그대로 써 줘.

Website hero cover illustration, wide 16:9, at least 1920px wide.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, deep teal light with warm amber accents and a little purple, medium brightness.
Scene: inside the same night lab world, one glowing golden thread crosses the whole scene from left to right, stringing together a row of small floating objects in order: a paper flowchart with diamond shapes, a fish on a scale, a tiny neural network, a small maze, a stack of word cards, a web of glowing threads, a speech bubble, a hand holding a wrench, a looping circular arrow, a conductor's baton and a drawer of index cards. At the far right the thread enters a tall glowing diamond-shaped gate standing like a doorway.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center following the thread with a finger, reflective;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding the end of the thread near the start, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, looking at the first flowchart object with a nod, finally convinced;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, standing beside the diamond gate and sliding one abacus bead, content.
Visual metaphor of the topic: one thread — try, check, improve — runs through every chapter and ends at the rule gate.
Composition: keep the upper middle area (from 25% to 75% of the width, top 30% of the height) as a dark, simple, empty lab wall for a title; keep every face and hand inside the band from 35% to 85% of the height and inside 10% side margins; main props large and crisp.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```
