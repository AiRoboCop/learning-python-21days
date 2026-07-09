# Day 9 학습 일지 — tkinter GUI 기초 + 커밋 컨벤션

**날짜**: 2026-06-19 (목)
**학습자**: 김윤종 (부산)
**특징**: GUI 세계 입문! 검은 콘솔 → 진짜 창

---

## 🎯 오늘의 목표 달성도

- [x] day09 환경 준비 (tkinter 테스트)
- [x] tkinter 이름 유래 이해
- [x] 첫 창 띄우기
- [x] 위젯 (Label, Button, Entry)
- [x] command로 버튼-함수 연결
- [x] .get() / .config()
- [x] lambda로 인자 전달
- [x] 커밋 컨벤션
- [x] 대시보드 + 역량 로드맵 갱신

---

## 📚 배운 것

### 🖥️ GUI 기초 — C1

- tkinter = Tk(GUI 툴킷) + interface (연결)
- Tk/Tcl: 1991년 탄생, 여러 언어가 가져다 씀
- 기본 tkinter는 다소 투박하지만, 내부 도구엔 최적!
  · ttk/테마로 개선 가능 (Day 12)
- CLI(콘솔) vs GUI(창+버튼)

### 🪟 첫 창

- import tkinter as tk (별명 관례)
- root = tk.Tk() → 창 객체 생성 (Day 7 OOP와 같은 구조!)
- root.title("제목") → 제목 표시줄
- root.geometry("400x300") → 크기 (가로x세로, x는 구분자)
- root.mainloop() → 창 유지 (필수! 없으면 바로 사라짐)
- GUI = 이벤트 대기 방식 (콘솔의 순차 실행과 다름)

### 🧩 위젯 (화면 부품)

- 2단계 패턴: 생성 + 배치(pack)
  · tk.Label(root, text="글자") → 생성
  · label.pack() → 배치 (없으면 안 보임!)
- Label(글자), Button(버튼), Entry(입력창)
- 첫 인자 root = "이 위젯의 부모 창"
- 옵션: text, font, fg(글자색), bg(배경색), pack(pady=여백)

### ⚡ 상호작용 (핵심!)

- command=함수 → 버튼에 함수 연결 (괄호 없이!)
  · command=say_hello (O) / command=say_hello() (X, 즉시 실행됨)
- entry.get() → 입력창의 값 가져오기
- label.config(text=...) → 위젯 내용 나중에 변경 (화면 동적 갱신)
- 이벤트(클릭) → 콜백(함수) → 반응(화면 변경)

### 🔧 lambda (인자 있는 함수 연결)

- command=lambda: 함수(인자) → 인자 있는 함수도 연결 가능!
- lambda = 이름 없는 미니 함수 (지연 실행 포장)
- 예: command=lambda: show_fruit("사과")
- 여러 버튼이 같은 함수를 다른 인자로 재사용

### 🔀 커밋 컨벤션 — C4

- 형식: "타입: 설명"
- 주요 타입:
  · feat: 새 기능 (가장 많이!)
  · fix: 버그 수정 (가장 많이!)
  · docs: 문서 / style: 스타일 / refactor: 구조개선
  · test: 테스트 / chore: 잡일
- 좋은 메시지 3원칙: 타입으로 시작 / 구체적 / 간결(50자)
- 예: feat: tkinter GUI 인사 프로그램 추가
- 커밋 = 미래의 나/동료에게 보내는 편지

---

## 🔗 역량 로드맵 연결

- **C1 AI코딩** (57→63%): tkinter GUI 실전! 이벤트→콜백 패턴, 첫 화면 프로그램
- **C4 Git협업** (58→61%): 커밋 컨벤션으로 깔끔한 히스토리 관리

---

## 💻 작성한 코드

- first_window.py (첫 창)
- widgets.py (라벨, 버튼)
- greeting_app.py (인사 프로그램 - 입력+버튼 연동!)
- learn_command.py (command 괄호 실험)
- learn_config.py (카운터 - command+config)
- learn_lambda.py (과일 선택 - lambda 인자)

---

## 🤔 오늘의 질문들 (논리를 파고듦!)

- tkinter 이름? → Tk + interface
- Windows UI와 다른가? → 투박하지만 내부 도구엔 최적
- tk.Tk()가 객체 생성? → Day 7 OOP로 스스로 해석 ✅
- command에 인자 있는 함수는? → 논리적 모순 발견 → lambda!

---

## 🚀 다음 (Day 10)

- 레이아웃 심화 (pack / grid / Frame)
- 위젯을 원하는 위치에 정교하게 배치하기

---

## 💭 오늘의 한 줄 회고

"검은 콘솔을 벗어나 진짜 창을 띄웠다.
버튼을 누르니 화면이 반응하는 순간,
'진짜 프로그램'을 만든 기분이었다.
그리고 command의 모순을 파고들어 lambda를 만났다."

---

## 🎯 21일 진척도

- [x] **Week 1 (Day 1~7)**: Python 기초 + Git/GitHub
- [x] **Day 8**: OOP 2 + JSON + 코드 포매터
- [x] **Day 9**: tkinter GUI 기초 + 커밋 컨벤션 ✅
- [ ] Day 10~14: GUI 심화 + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
