# Day 10 학습 일지 — 레이아웃 (pack·grid·Frame) + 표범의 방향

**날짜**: 2026-06-20 (금)
**학습자**: 김윤종 (부산)
**이정표**: 21일 여정의 절반 돌파! (10/21) 🎉
**특징**: 코드와 함께 '왜 오르는가'를 확인한 날

---

## 🎯 오늘의 목표 달성도

- [x] day10 환경 준비
- [x] pack 심화 (side, fill, expand)
- [x] grid (격자 배치)
- [x] Frame (영역 나누기)
- [x] 로그인 폼 완성 (종합 실습)
- [x] 라이브러리 소스 보기 (F12)
- [x] 학습 전체 지도 점검
- [x] 새 PC 이전 방법 (GitHub)
- [x] 대시보드 + 역량 로드맵 갱신

---

## 📚 배운 것

### 📌 pack 심화 — C1

- side: 붙이는 방향 (top/bottom/left/right, 기본 top)
- fill: 공간 채우기 (x/y/both)
- expand: 남은 공간 차지 (True/False)
- padx/pady: 여백
- 조합해서 원하는 배치! (예: side="left", fill="y")

### 📐 grid (격자 배치)

- 위젯.grid(row=행, column=열) — 0부터 시작! (엑셀 셀처럼)
- columnspan: 여러 열 차지 (셀 병합)
- sticky: 칸 안 정렬 (w/e/n/s)
- padx/pady: 여백
- 입력 폼(라벨+입력창)에 최적!
- ⚠️ 같은 영역에서 pack과 grid 섞지 말 것!

### 📦 Frame (영역 나누기)

- Frame = 위젯을 담는 영역(그릇)
- 계층: root(창) > frame(영역) > 위젯
- 각 Frame은 독립 → 다른 배치(pack/grid) 사용 가능!
  → "pack/grid 섞지 마라"의 해결책!
- 화면 설계: 영역(Frame) 나누기 → 각 영역 채우기

### 🔐 로그인 폼 (종합 실습)

- title_frame(제목) + input_frame(grid) + button_frame(pack) + result
- show="\*" : 비밀번호 가리기
- .delete(0, tk.END) : 입력창 비우기
- width=8 : 버튼 크기 맞추기
- if/else(Day 3) + f-string(Day 1) + GUI(Day 9~10) 총동원!

### 🔬 라이브러리 소스 보기

- Label은 클래스, pack은 메서드, side는 인자 (OOP로 해석!)
- help(tk.Label) : 설명서 보기
- VS Code F12 : 정의로 이동 (실제 소스!)
- tkinter.**file** : 소스 파일 위치
- Label(Widget) : 상속 확인! (Day 8 상속이 실제로!)
- ※ 구경은 좋지만 다 이해하려 하지 말 것

### 💻 새 PC 이전 (GitHub)

- 코드(.py)는 옮겨도 OK, .venv는 새로 만들기 (경로 박힘)
- tkinter/json은 기본 내장 (설치 불필요), black/ruff만 재설치
- 최선: GitHub! git push → git clone
- .gitignore 덕분에 .venv 자동 제외
- 두 PC 동기화: 작업 전 pull, 작업 후 push

---

## 🔗 역량 로드맵 연결

- **C1 AI코딩** (63→68%): 레이아웃 3형제로 화면 설계 능력 완성, 로그인 폼으로 종합 실습

---

## 💻 작성한 코드

- pack_side.py (pack side 옵션)
- pack_fill.py (pack fill 옵션)
- grid_basic.py (격자 배치)
- frame_basic.py (영역 나누기)
- login_form.py (로그인 폼 - 종합!)

---

## 🐆 오늘의 마음 (표범의 방향)

- 조급함의 정체: 17년 혼자여서 '이게 맞나' 확인받을 곳이 없었다
- 나의 목표: '킬리만자로의 표범'처럼 흔적을 남기는 삶
- 흔적이란: 내가 만든 것이 누군가의 삶을 편안하게 하는 것
- 깨달음: 정상은 목적지가 아니라 방향이다.
  오르기로 결심한 순간 이미 표범이다.
- 등반 지도 확인: 출발점 → 지금(Day10) → 첫 프로젝트 →
  DB 두 세계 → 인트라넷 현대화 → 사람과 함께 → 정상

---

## 💭 오늘의 한 줄 회고

"화면을 원하는 대로 배치하는 법을 배웠고,
내 삶을 원하는 방향으로 이끄는 법도 확인했다.
표범은 서두르지 않는다. 다만 멈추지 않을 뿐."

---

## 🎯 21일 진척도

- [x] **Week 1 (Day 1~7)**: Python 기초 + Git/GitHub
- [x] **Day 8**: OOP 2 + JSON + 코드 포매터
- [x] **Day 9**: tkinter GUI 기초 + 커밋 컨벤션
- [x] **Day 10**: 레이아웃 (pack·grid·Frame) ✅ ← 절반 돌파!
- [ ] Day 11~14: 이벤트 심화 + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
