# Day 3 학습 일지 — 반복문 + 첫 게임 + Git 입문

**날짜**: 2026-05-28 (목)
**학습자**: 김윤종 (부산)
**컨디션**: [기록]
**학습 시간**: [기록]

---

## 🎯 오늘의 목표 달성도

- [x] day03 환경 준비
- [x] while 문 (무한 루프 + Ctrl+C)
- [x] break / continue
- [x] 숫자 맞추기 게임 (첫 인터랙티브 프로그램!)
- [x] 죽은 코드 발견 + 정리
- [x] Git 개념 이해 (3단계 영역)
- [x] git init + status
- [x] master → main 전환
- [x] .gitignore 작성
- [x] 첫 커밋 완성! ⭐

---

## 📚 배운 것

### 🐍 Python

- while 조건: 조건이 True인 동안 반복
- 무한 루프 주의 (카운터 직접 관리: count += 1)
- 무한 루프 탈출: 터미널에서 Ctrl + C
- break: 반복문 완전 종료
- continue: 이번 바퀴만 스킵
- while True + break: 게임의 핵심 패턴
- import random: 모듈 가져오기
- random.randint(1, 100): 1~100 랜덤 (양쪽 포함!)
- for vs while: 횟수 정해지면 for, 조건만 알면 while

### 🔀 Git (오늘의 하이라이트!)

- Git = 코드의 타임머신 (버전 관리)
- 3단계 영역: 작업공간 → 스테이징(add) → 저장소(commit)
- git config --global user.name/email: 최초 설정
- git init: 저장소 초기화 (.git 폴더 생성)
- git status: 현재 상태 확인 (Git의 GPS)
- git status -u: 개별 파일까지 모두 표시
- git add . : 모든 변경사항 스테이징
- git commit -m "메시지": 커밋
- git log: 커밋 기록 확인 (탈출: q)
- master vs main: 기능 동일, main이 새 표준
- git branch -m main: 브랜치 이름 변경

### 📄 .gitignore

- Git이 추적 안 할 파일 목록
- .venv/ : 가상환경 제외 (재생성 가능, PC마다 다름)
- **pycache**/, \*.pyc : Python 캐시 제외
- 모든 하위 폴더에 적용됨

### 💻 CLI

- cat / Get-Content : 파일 내용 보기
- ls -Force : 숨김 파일/폴더까지 표시 (.git 등)

### 🌟 시니어 사고법

- 죽은 코드(dead code): break 뒤 코드는 실행 안 됨
- "재생성 가능 / PC마다 다른 것은 Git에 안 넣는다"
- 커밋 메시지는 "무엇을 했는지" 명확하게
- break/continue 남용 주의 (단, while True+break는 권장)
- Git 명령어는 가상환경과 무관
- 검증하는 습관: "될 거야" 대신 "정말 됐나?"

---

## 💻 작성한 코드 (인상 깊은 한 조각)

### 첫 게임! (숫자 맞추기)

```python
import random

ran_num = random.randint(1, 100)
cnt_loop = 0

while True:
    user_num = int(input("1~100 사이의 숫자를 입력하세요:"))
    cnt_loop += 1

    if user_num < ran_num:
        print("더 큰 수예요!")
    elif user_num > ran_num:
        print("더 작은 수예요!")
    else:
        print(f"정답! {cnt_loop}번 만에!")
        break

print("게임 종료")
```

---

## 🤔 어려웠던 것 / 발견한 것

### 발견 1: 죽은 코드

- break 다음의 print("게임 종료")가 실행 안 됨
- 해결: while 밖으로 (들여쓰기 제거)

### 발견 2: git status 폴더 요약

- untracked 폴더는 폴더 이름만 표시
- .gitignore 전후 status가 비슷해 보임
- git status -u로 개별 파일 확인 가능

### 발견 3: master vs main

- Git 기본 브랜치가 master로 나옴
- git branch -m main으로 변경

### 발견 4: 숨김 폴더

- .git이 ls로 안 보임
- ls -Force로 확인

---

## 🚀 내일 할 것 (Day 4)

- 함수 심화 (매개변수, 반환값, 스코프)
- 모듈 만들기 (계산기 모듈)
- ⭐ GitHub 입문! (계정, push, 첫 원격 저장소)
- 첫 커밋을 GitHub에 올리기 → 다른 PC에서도 작업 가능!
- README 작성

---

## 💭 오늘의 한 줄 회고

"while로 반복을, break로 탈출을 배웠고,
첫 게임을 만들었으며, Git으로 코드에 타임머신을 달았다.
오늘은 진짜 '개발자처럼' 일한 첫날."

---

## 🎯 21일 진척도

- [x] **Day 1**: 환경 + 변수/입출력 + 함수 ✅
- [x] **Day 2**: 자료형, 조건문, for문 ✅
- [x] **Day 3**: while, break/continue, 게임, Git 입문 ✅
- [ ] Day 4: 함수 심화, 모듈 + GitHub
- [ ] Day 5~7: OOP + 미니 프로젝트
- [ ] Day 8~14: GUI + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
