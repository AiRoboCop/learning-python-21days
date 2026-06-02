# Day 1 학습 일지 — 모던 Python 첫걸음

**날짜**: 2026-05-26 (화)
**학습자**: 김윤종
**위치**: 부산
**컨디션**: [기록]
**학습 시간**: [기록]

---

## 🎯 오늘의 목표 달성도

- [x] PowerShell 7 (pwsh) 설치
- [x] Python 3.14.4 설치 확인
- [x] VS Code + Python 확장 + Pylance + Debugger
- [x] 학습 폴더 D:\learning_python_21days\day01 생성
- [x] 가상환경 .venv 생성 + 활성화
- [x] hello.py 첫 실행 ⭐
- [x] 변수, input(), f-string 학습
- [x] 첫 에러 만나기 (TypeError) + 해결
- [x] 미션 1: 자기소개 프로그램 ⭐
- [x] 리팩토링 4단계 완주 (v1.0 → v1.4) ⭐⭐⭐
- [ ] 미션 2: BMI 계산기 (Day 2로 이월)
- [ ] 미션 3: 사칙연산 계산기 (Day 2로 이월)

---

## 📚 배운 것

### 🐍 Python 핵심

- 변수: 값에 이름표 붙이기 (`name = "김윤종"`)
- 4가지 기본 타입: str, int, float, bool
- `input()`: 항상 문자열(str) 반환 ← 함정!
- `int()`, `float()`: 타입 변환
- `type()`: 타입 확인
- f-string: `f"이름: {name}"`
- 함수: `def 함수이름() -> 타입:`
- 딕셔너리: `{"키": 값}` 형태로 관련 데이터 묶기
- 메인 가드: `if __name__ == "__main__":`
- 타입 힌트: `def 함수(매개변수: 타입) -> 반환타입:`

### 💻 CLI 명령어

- `pwd` — 현재 위치
- `cd 경로` — 폴더 이동
- `mkdir 이름` — 폴더 생성
- `ls` — 폴더 내용 보기
- `code .` — 현재 폴더를 VS Code로 열기
- `python 파일명.py` — Python 파일 실행
- `python -m venv .venv` — 가상환경 생성
- `.\.venv\Scripts\Activate.ps1` — 가상환경 활성화
- `pip list` — 설치된 패키지 목록
- `$PSVersionTable` — PowerShell 버전 확인
- `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` — PS 보안 정책

### 🔧 VS Code 단축키

- `Ctrl + Shift + P` — Command Palette (만능 검색) ⭐⭐⭐
- `Ctrl + Shift + X` — 확장 관리
- `Ctrl + Shift + E` — 파일 탐색기
- `` Ctrl + ` `` — 터미널 열기
- `Ctrl + S` — 저장
- `Ctrl + N` — 새 파일
- 탭 자동완성 — 명령어/경로 빠르게 입력

### 🌟 시니어 사고법

- "Python 프로젝트 = 가상환경 먼저. 예외 없음."
- "함수는 한 가지 일만 한다" (단일 책임 원칙, SRP)
- "코드는 작성되는 횟수보다 읽히는 횟수가 훨씬 많다" (Guido van Rossum)
- "코드를 두 번 짜라. 작동하게, 그리고 아름답게" (Kent Beck)
- "변수는 명사, 함수는 동사로 시작"
- "안 보인다 ≠ 안 된다"
- "에러는 적이 아니라 선생님"
- "마우스는 1회용, 키보드는 평생용"

---

## 💻 작성한 코드 (인상 깊은 한 조각)

### 첫 Python 코드

```python
print("Hello, Python!")
print("나는 21일 후 GUI 프로그램을 만든다!")
```

### 시니어 완성형 (v1.4)

```python
def get_user_info() -> dict:
    """사용자에게서 자기소개 정보를 입력받아 딕셔너리로 반환"""
    name = input("이름이 뭐예요? ")
    age = int(input("나이가 몇이에요? "))
    city = input("어디 사세요? ")
    favorite_food = input("좋아하는 음식은? ")

    return {
        "name": name,
        "age": age,
        "city": city,
        "favorite_food": favorite_food,
    }


def print_introduction(user: dict) -> None:
    """입력받은 user 딕셔너리를 바탕으로 자기소개 출력"""
    print("-" * 30)
    print(f"안녕하세요! 저는 {user['name']}입니다.")
    # ... (생략)
    print("-" * 30)


def main() -> None:
    """프로그램의 메인 흐름"""
    user_info = get_user_info()
    print_introduction(user_info)


if __name__ == "__main__":
    main()
```

이 패턴이 21일 후 짤 768줄짜리 프로그램의 뼈대다.

---

## 🤔 어려웠던 것 / 만난 에러

### 발견 1: pwsh vs powershell

- 같은 건 줄 알았는데 다른 프로그램이었음
- pwsh = 7.x (최신, 크로스 플랫폼)
- powershell = 5.1 (구버전, Windows 전용)
- 교훈: 모르는 명령어는 그냥 쓰지 말고 짚고 넘어가기

### 발견 2: VS Code 상태바 표시 형식

- 가이드에 나온 모양과 실제가 달라서 "안 보인다"고 생각
- 사실은 더 짧은 형식(`🐍 .venv (3.14.4)`)으로 잘 표시되어 있었음
- 교훈: "안 보인다 ≠ 안 된다"

### 첫 Python 에러: TypeError

- `print(user_age + 10)` 에서 발생
- `TypeError: can only concatenate str (not "int") to str`
- 원인: `input()`은 항상 문자열 반환
- 해결: `int(input(...))`로 감싸기

---

## 🚀 내일 할 것 (Day 2)

- 미션 2: BMI 계산기
- 미션 3: 사칙연산 계산기
- Day 2 정규 주제: 자료형, 조건문(if/elif/else), 반복문(for/while)
- VS Code 단축키 10개 추가 학습
- Pylance 자동완성 본격 활용

---

## 💭 오늘의 한 줄 회고

"23년 경력의 가면을 벗고, 깨끗한 초심자로 다시 시작한 첫날.
14개의 마일스톤을 통과하며 모던 개발자로 가는 문을 열었다."

---

## 🎯 21일 학습 진척도

- [x] **Day 1**: 환경 구축 + 변수/입출력/f-string + 함수 맛보기 ✅
- [ ] Day 2: 자료형, 조건문, 반복문
- [ ] Day 3: 함수 심화, 모듈, 예외 처리 + Git 입문
- [ ] Day 4: 리스트/딕셔너리, 파일 I/O + GitHub 입문
- [ ] Day 5: 클래스 기초 (OOP 1) + VS Code 디버거
- [ ] Day 6: 상속, 다형성 (OOP 2) + Git 브랜치
- [ ] Day 7: JSON, 예외 심화 + 미니 프로젝트(콘솔 가계부)
- [ ] Day 8~14: Week 2 — GUI + 비동기 + DB
- [ ] Day 15~21: Week 3 — 시니어 마인드 + 최종 프로젝트
