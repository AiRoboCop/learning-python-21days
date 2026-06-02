# Day 2 학습 일지 — 조건문과 반복문

**날짜**: 2026-05-27 (수)
**학습자**: 김윤종 (부산)
**컨디션**: [기록]
**학습 시간**: [기록]

---

## 🎯 오늘의 목표 달성도

- [x] day02 환경 준비 (폴더, .venv)
- [x] bool 자료형 + Truthy/Falsy
- [x] 비교 연산자 (==, !=, >, <, >=, <=)
- [x] 논리 연산자 (and, or, not)
- [x] if 문
- [x] if-else
- [x] if-elif-else
- [x] BMI 등급 메시지 추가 (어제 미룬 도전!)
- [x] for 문 (Day 3 미리보기)
- [ ] while 문 (Day 3로)
- [ ] 숫자 맞추기 게임 (Day 3로)

---

## 📚 배운 것

### 🐍 Python 핵심

- bool: True / False (첫 글자 대문자, 따옴표 없음)
- Truthy/Falsy: 0, "", [], {}, None은 False / 나머지는 True
- 비교 연산자: ==, !=, >, <, >=, <=
- 체이닝: 20 <= age < 30 (수학식처럼! Python의 특권)
- 논리 연산자: and(둘 다), or(하나라도), not(반대)
- 단락 평가: x != 0 and 1/x > 0.5 (안전 가드)
- if / if-else / if-elif-else
- 첫 True에서 멈춤 (elif 핵심)
- for 문 + range()
- range는 끝 숫자 미포함! range(1,6) → 1~5
- 누적 패턴: total += i

### 🚨 가장 중요한 깨달음

- = (할당) vs == (비교) 구분 (VBScript와 다름!)
- 범위 검사 순서 함정 (큰 값부터 또는 체이닝으로)
- "프로그램이 작동한다 ≠ 옳다" (조용한 논리 버그)

### 💻 CLI 명령어 (파일 조작)

- ni / New-Item : 파일 생성
- cp / Copy-Item : 복사
- mv / Move-Item : 이동/이름변경
- rm / Remove-Item : 삭제 (휴지통 안 거침!)
- cat / Get-Content : 내용 보기
- rm 안전장치: -WhatIf (시뮬레이션), -Confirm (확인)

### 🌟 시니어 사고법

- "if를 적게 쓸 줄 아는 사람이 잘 하는 사람"
- 함수 이름은 동작과 일치 (print* vs get*)
- 데이터(등급)와 표현(출력 형식) 분리
- if에는 긍정형 조건을
- "범위 검사는 한쪽 극단부터 순서대로"
- 사용자 입력은 .upper()/.strip()으로 정규화
- 부동소수점은 == 대신 차이 비교

### 💭 학습 방향 확신

- AI 시대: 읽기/지시/판단 능력이 핵심. 기초가 더 중요
- Python: 내 목표(인트라넷+GUI+AI)에 정확히 맞는 선택
- "언어 5%, 꾸준함 95%"

---

## 💻 작성한 코드 (인상 깊은 한 조각)

### 체이닝 + elif 결합 (학습 전이!)

```python
def get_bmi_grade(bmi: float) -> str:
    """BMI 수치를 받아 등급 문자열을 반환"""
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 23:    # 어제 배운 체이닝!
        return "정상 체중"
    elif 23 <= bmi < 25:
        return "과체중"
    else:
        return "비만"
```

### 구구단 (반복문의 힘)

```python
dan = int(input("몇 단? "))
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")
```

---

## 🤔 어려웠던 것 / 만난 함정

### 함정 1: = vs ==

- VBScript는 = 하나로 비교했지만, Python은 엄격히 구분
- = (할당), == (비교)

### 함정 2: range 끝 미포함

- range(1, 6) → 6은 포함 안 됨 (1~5)
- off-by-one 버그의 원인

### 함정 3: elif 순서 (조용한 버그)

- 작은 값부터 검사하면 큰 값이 엉뚱하게 걸림
- 해결: 큰 값부터 또는 체이닝으로 범위 명시

### 개선점 (다음에 적용)

- 함수 이름 print_bmi_msg → get_bmi_grade (return하므로)
- 반환 문자열에 기준 섞지 않기 ("비만"만 반환)

---

## 🚀 내일 할 것 (Day 3)

- while 문 + break / continue
- 숫자 맞추기 게임 (Day 2 산출물 완성!)
- 함수 심화, 모듈
- 예외 처리 기초
- ⭐ Git 입문! (init, add, commit, .gitignore)
- 첫 커밋으로 오늘까지의 코드 저장

---

## 💭 오늘의 한 줄 회고

"조건문으로 코드에 갈림길을, 반복문으로 수레바퀴를 달았다.
그리고 '내가 가는 길'에 대한 확신을 두 배로 키운 날."

---

## 🎯 21일 진척도

- [x] **Day 1**: 환경 구축 + 변수/입출력/f-string + 함수 ✅
- [x] **Day 2**: 자료형, 조건문, 비교/논리 연산자, for문 ✅
- [ ] Day 3: 반복문(while), 함수 심화, 예외 + Git 입문
- [ ] Day 4: 리스트/딕셔너리, 파일 I/O + GitHub
- [ ] Day 5~7: OOP + 미니 프로젝트
- [ ] Day 8~14: GUI + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
