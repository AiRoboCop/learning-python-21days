# Day 1 학습 일지

**날짜**: 2026-05-26 (화)
**학습 시간**: [본인이 채워주세요]
**컨디션**: [본인이 채워주세요]

---

## 🎯 오늘의 목표 (달성도)

- [x] PowerShell 7 (pwsh) 설치
- [x] Python 3.14.4 설치 확인
- [x] VS Code 설치 + Python 확장
- [x] 학습 폴더 생성
- [x] 가상환경 .venv 생성 + 활성화
- [x] VS Code 인터프리터 연결
- [x] hello.py 첫 실행
- [x] 변수/input/f-string 학습
- [ ] 미션 3개 (내일로 미룸)

---

## 📚 배운 것

### Python 핵심 개념

- **변수**: 값에 이름표를 붙이는 것 (`name = "박상현"`)
- **4가지 기본 타입**: `str` (문자열), `int` (정수), `float` (실수), `bool` (참/거짓)
- **`input()`**: 사용자 입력. **항상 문자열을 반환**한다는 함정 주의!
- **`int()`, `float()`**: 문자열을 숫자로 변환
- **`type()`**: 변수의 타입 확인
- **f-string**: `f"이름: {name}, 나이: {age}"` — 현대 Python 표준

### 변수 이름 짓기 규칙 (시니어 스타일)

- snake_case (소문자 + 언더스코어)
- 약자보단 풀어쓰기 (`user_name` > `un`)
- 단위 명시 (`height_cm`, `time_ms`)
- bool은 `is_`, `has_`, `can_` 접두사

### CLI 명령어

- `pwd` — 현재 위치
- `cd 경로` — 폴더 이동
- `mkdir 이름` — 폴더 생성
- `ls` — 폴더 내용 보기
- `code .` — 현재 폴더를 VS Code로 열기
- `python --version` — Python 버전 확인
- `python -m venv .venv` — 가상환경 생성
- `.\.venv\Scripts\Activate.ps1` — 가상환경 활성화
- `pip list` — 설치된 패키지 목록
- `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` — PS 보안 정책 변경

### VS Code 단축키

- `Ctrl + Shift + P` — Command Palette (만능 검색) ⭐⭐⭐
- `Ctrl + Shift + X` — 확장 관리
- `Ctrl + Shift + E` — 파일 탐색기
- `` Ctrl + ` `` — 터미널 열기
- `Ctrl + S` — 저장
- `Ctrl + N` — 새 파일

### 개념적 깨달음

- **가상환경의 중요성**: "프로젝트마다 다른 책상" — 전역 환경 오염 방지
- **`.venv` 이름이 좋은 이유**: 숨김 파일 관례, VS Code 자동 인식, Python 공식 권장
- **CLI는 평생 자산**: 마우스 클릭 100번 < 명령어 1줄
- **에러 메시지는 선생님**: 무서워하지 말고 끝까지 읽기

---

## 💻 작성한 코드 (인상 깊은 한 조각)

```python
# 나의 첫 Python 코드 - 2026-05-26
print("Hello, Python!")
print("나는 21일 후 GUI 프로그램을 만든다!")

# f-string의 우아함을 처음 경험한 순간
name = "박상현"
age = 30
print(f"저는 {name}이고, {age}살입니다.")
print(f"내년이면 {age + 1}살이 됩니다.")
```

---

## 🤔 어려웠던 것 / 만난 에러

### 에러 1: PSEdition 차이를 모름

- **현상**: `pwsh` 와 `powershell` 이 같은 건 줄 알았음
- **해결**: 둘은 다른 프로그램! `pwsh` = 7.x (최신), `powershell` = 5.1 (구버전)
- **교훈**: 모르는 명령어는 그냥 쓰지 말고 한 번 짚고 넘어가기

### 에러 2: 상태바에서 인터프리터를 못 찾음

- **현상**: 가이드에 있던 표시 형식이 안 보임
- **원인**: VS Code 최신 버전에서 표시 형식이 짧아짐 (`🐍 .venv (3.14.4)`)
- **교훈**: "안 보인다 ≠ 안 된다". 기대한 모양이 아닐 수 있음

### 첫 Python 에러: TypeError

- **현상**: `print(user_age + 10)` 에서 `TypeError: can only concatenate str (not "int") to str`
- **원인**: `input()`은 항상 문자열 반환
- **해결**: `int(input(...))` 로 감싸기

---

## 🚀 내일 할 것 (Day 2 예고)

- 미션 3개 마무리 (오늘 못한 부분)
  - 자기소개 프로그램
  - BMI 계산기
  - 사칙연산 계산기
- Day 2 주제: **자료형, 조건문(if/elif/else), 반복문(for/while)**
- VS Code 단축키 10개 (Ctrl+/, Alt+클릭 등)
- Pylance 자동완성 본격 활용

---

## 🌟 오늘의 시니어 명언

> "Python 프로젝트 = 가상환경 먼저. 예외 없음."
> "마우스는 1회용, 키보드는 평생용."
> "에러는 적이 아니라 선생님이다."
