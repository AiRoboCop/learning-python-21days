# Day 5 학습 일지 — 자료구조 + 파일 I/O + 디버거

**날짜**: 2026-06-09 (월)
**학습자**: 김윤종 (부산)
**컨디션**: [기록]
**학습 시간**: [기록]

---

## 🎯 오늘의 목표 달성도

- [x] day05 환경 준비
- [x] 리스트 (list)
- [x] 딕셔너리 (dict)
- [x] 튜플 + 세트
- [x] 파일 I/O (읽기/쓰기)
- [x] iterable·next() 이해
- [x] while로 파일 읽기
- [x] VS Code 디버거
- [x] AI 검증 경험 (PATHEXT) ⭐
- [x] 대시보드 + 역량 로드맵 갱신

---

## 📚 배운 것

### 🐍 자료구조 (4종)

- 리스트 [ ]: 순서O, 변경O, 인덱스 0부터!
- fruits[0] 첫 번째, fruits[-1] 마지막
- append(), len(), for item in list
- 딕셔너리 { }: 키-값, person["name"]
- for key, value in dict.items()
- 튜플 ( ): 변경 불가 (Day 4 "여러 값 반환"이 사실 튜플!)
- 세트 { }: 중복 제거, set([1,2,2]) → {1,2}
- 실무 형태: [{"name":..., "dept":...}, {...}] (DB 데이터!)

### 📄 파일 I/O

- with open("f", "w", encoding="utf-8") as f
- f.write("내용\n") — \n 직접!
- f.read() 전체 / for line in f 줄 단위
- 모드: "w"(덮어씀) "r"(읽기) "a"(추가)
- encoding="utf-8" 필수 (한글!)

### 🔁 iterable·next() (깊은 이해!)

- 리스트·문자열·파일 = 모두 iterable
- for = next() 자동 반복 (끝나면 StopIteration)
- f는 파일 객체, for line in f → 한 줄씩
- f.read()는 문자열 → for하면 글자 하나씩
- readline(): 끝에서 "" 반환 → while True+break
- lazy 읽기 = 메모리 효율 (큰 파일도 안전)

### 🔧 VS Code 디버거

- 중단점 🔴 (줄번호 왼쪽 클릭)
- F5 시작, F10 한 줄 실행, F11 함수 안으로
- VARIABLES 패널에서 변수 변화 실시간 관찰
- for문 변수가 바뀌는 걸 눈으로 확인!
- print 디버깅 vs 디버거 (복잡한 건 디버거)

### ⚙️ 환경 (검증으로 배움!)

- 디버거는 .venv 활성화 대신 python.exe 직접 경로 실행
- (.venv) 표시 없어도 가상환경 사용 중
- Activate = Activate.ps1 (PowerShell이 .ps1 자체 인식)
- PATHEXT엔 .PS1 없음! (AI가 틀렸고, 내가 검증으로 발견)

### 🌟 시니어 사고법

- 적절한 그릇 선택 = 짧고 명확한 코드
- 표시가 아니라 실제(python.exe 경로)를 본다
- AI도 틀린다 → 직접 검증한다 (오늘 실증!)

---

## 🔗 역량 로드맵 연결 (오늘부터!)

- **C2 자료구조**: 오늘 직접 학습! (리스트·딕셔너리·튜플·세트 + 파일 I/O) → 50%→65%
- **C1 AI 코딩 습관**: PATHEXT 검증으로 AI 오류를 잡아냄 = "AI를 검증하는" 핵심 경험 → 35%→42%
- 오늘 배운 [{"name":..}, {..}] 형태는 Phase 3(C3 DB)에서 그대로 쓰임

---

## 💻 작성한 코드

- learn_list.py (리스트)
- learn_dict.py (딕셔너리)
- learn_tuple_set.py (튜플·세트)
- learn_file.py (파일 I/O)
- learn_iterable.py (iterable·next)
- learn_while_file.py (while 파일 읽기)
- learn_debug.py (디버거 연습)

---

## 🤔 어려웠던 것 / 발견한 것

### 발견 1: for문의 비밀 (iterable)

- f는 파일 객체인데 for line in f가 한 줄씩?
- → 파일 객체가 iterable, next() 자동 반복

### 발견 2: AI(Claude)도 틀린다!

- "PATHEXT에 .PS1 있다" → 직접 확인하니 없음!
- → AI를 의심하고 검증하는 게 핵심 (C1)

### 발견 3: 가상환경의 두 얼굴

- (.venv) 표시 vs 실제 python.exe 경로
- 표시 없어도 가상환경 쓰는 중

---

## 🚀 내일 할 것 (Day 6)

- 예외 처리 (try / except) — 에러를 우아하게 다루기
- Git 브랜치 (branch) — 협업 Git의 시작 (C4 씨앗!)
- 파일 I/O와 예외 처리 연결 (파일 없을 때 대비)

---

## 💭 오늘의 한 줄 회고

"자료구조 4종을 손에 넣었고, 파일을 읽고 쓰게 됐으며,
for문의 비밀(iterable)까지 파고들었다.
그리고 무엇보다 — AI도 틀린다는 걸 직접 검증으로 확인하며,
'AI와 함께 발전하는 개발자'의 첫 걸음을 뗐다."

---

## 🎯 21일 진척도

- [x] **Day 1~4**: 환경·변수·조건·반복·함수·모듈·GitHub ✅
- [x] **Day 5**: 자료구조·파일 I/O·디버거 ✅
- [ ] Day 6: 예외 처리 + Git 브랜치
- [ ] Day 7: 클래스(OOP) + 첫 PR + 미니 프로젝트
- [ ] Day 8~14: GUI + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
