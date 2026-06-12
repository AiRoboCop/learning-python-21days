# Day 6 학습 일지 — 예외 처리 + Git 브랜치 + 충돌 해결

**날짜**: 2026-06-12 (금)
**학습자**: 김윤종 (부산)
**컨디션**: [기록]
**학습 시간**: [기록]

---

## 🎯 오늘의 목표 달성도

- [x] day06 환경 준비
- [x] try/except 기본
- [x] 에러 종류 파악 (type(e).**name**)
- [x] 예외 탐정 연습
- [x] 여러 except + else + finally
- [x] 파일 I/O + 예외 결합
- [x] Git 브랜치 생성/이동/격리
- [x] git branch -m/-M 차이
- [x] 브랜치 병합 (merge)
- [x] merge conflict 해결 ⭐⭐⭐
- [x] 대시보드 + 역량 로드맵 갱신

---

## 📚 배운 것

### 🐍 예외 처리 (C1)

- try/except: 에러 나도 프로그램 안 죽게 (안전망)
- 흐름: 에러 없으면 except 건너뜀, 있으면 except 실행
- except 에러종류 as e: e로 에러 내용 받기
- 에러 종류 모를 때:
  · 빨간 메시지의 콜론 앞 단어 읽기
  · except Exception as e + type(e).**name**
- except Exception as e (권장) vs except: (bare, 비권장)
  · bare except는 Ctrl+C까지 잡아서 위험
- 여러 except: 에러마다 다르게 처리
- else: 에러 없을 때만 (성공 시)
- finally: 무조건 실행 (정리 작업, DB 닫기 등)
- 실행 순서: 성공→try→else→finally / 실패→try→except→finally
- 파일 + 예외: try { with open } except FileNotFoundError
- 절대 except: pass 로 에러 숨기지 말 것!

### 🔀 Git 브랜치 (C4)

- 브랜치 = 독립된 작업 공간 (나뭇가지/평행우주)
- git branch: 목록 (\* = 현재 위치)
- git switch -c 이름: 생성 + 이동
- git switch 이름: 이동
- git branch -m: 이름변경(안전) / -M: 강제 (대문자=강제!)
- git merge 브랜치: 병합 (받는쪽에서 주는쪽을)
- git branch -d: 안전삭제 / -D: 강제삭제
- 워크플로우: switch -c → 작업+커밋 → main → merge → branch -d

### ⚡ 브랜치 핵심 원리 (실험으로 발견!)

- 커밋이 파일을 브랜치에 "소속"시킨다
- 커밋 전: 작업공간에 떠 있음 (브랜치 공유, 모두 보임)
- 커밋 후: 그 브랜치 히스토리에 박제 (그 브랜치만)
- merge: 다른 브랜치로 소속 공유
- switch 시 git이 그 브랜치 히스토리에 맞춰 작업공간 재구성
- 커밋 안 된 변경이 충돌하면 switch 차단 (안전장치)

### 🔥 merge conflict (충돌 해결)

- 양쪽에서 같은 부분 다르게 수정 → 충돌
- 충돌 마커:
  <<<<<<< HEAD (현재 브랜치 내용)
  =======
  (병합 대상 내용)
  > > > > > > > 브랜치명
- 해결: 마커 편집(원하는 내용만) → git add → git commit
- VS Code 버튼: Accept Current/Incoming/Both
- git status: unmerged paths, both modified
- git merge --abort: 병합 취소 (안전망)

### 🌟 시니어 사고법

- 견고한 코드 = 예외 대비 (C1)
- 외부(파일·DB·네트워크)와 만나는 코드는 방어적으로
- 브랜치 = 안전하게 실패할 자유
- 충돌은 협업의 일상, 실패 아님
- 막히면 git status (현재 상태 + 다음 할 일 알려줌)
- 도구 화면(표시)이 아니라 실제(디스크)를 보라

---

## 🔗 역량 로드맵 연결

- **C1 견고한 코딩** (42→46%): 예외 처리로 에러에 강한 코드 작성
- **C4 Git 협업** (30→45%): 브랜치·병합·충돌 해결 = 협업 Git의 핵심! Phase 2 본격 진입 준비

---

## 💻 작성한 코드 / 실험

- learn_exception.py (try/except)
- learn_exception2.py (에러 종류 파악)
- exception_detective.py (예외 탐정)
- learn_exception3.py (여러 except + else + finally)
- learn_file_safe.py (파일 + 예외)
- 브랜치 실험: test.txt, branch_memo_3.txt (격리·충돌 실험)

---

## 🤔 어려웠던 것 / 발견한 것 (오늘의 하이라이트!)

### 발견 1: 브랜치 격리의 원리 (실험으로!)

- 커밋 전/후/merge에 따라 파일 가시성이 다름
- 결론: 커밋이 브랜치 소속을 결정한다

### 발견 2: merge conflict 정복

- 충돌을 스스로 만들고, 마커 해결 후 병합 완료
- 협업 Git의 핵심 관문 통과!

### 발견 3: switch 차단 = 안전장치

- 커밋 안 된 변경이 충돌하면 git이 switch를 막음
- 커밋하면 가능

### 발견 4: 도구의 진실

- PowerShell ls(실시간) vs 탐색기(캐시, F5 필요)
- 표시가 아니라 실제 디스크 상태가 진실

---

## 🚀 내일 할 것 (Day 7 — Week 1 마지막!)

- 클래스 (OOP 1) — 객체지향 프로그래밍 시작
- 첫 PR (Pull Request) — 협업 Git 다음 단계 (C4)
- 미니 프로젝트: 콘솔 가계부
- Week 1 완주! 🎉

---

## 💭 오늘의 한 줄 회고

"예외 처리로 코드를 견고하게 만들었고,
브랜치로 협업의 문을 열었으며,
merge 충돌이라는 가장 어려운 관문을 스스로 실험으로 정복했다.
나는 오늘 '실험하는 개발자'였다."

---

## 🎯 21일 진척도

- [x] **Day 1~5**: 환경·변수·조건·반복·함수·모듈·GitHub·자료구조·파일 ✅
- [x] **Day 6**: 예외 처리 + Git 브랜치 + 충돌 해결 ✅
- [ ] Day 7: 클래스(OOP) + 첫 PR + 미니 프로젝트 (Week 1 완주!)
- [ ] Day 8~14: GUI + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
