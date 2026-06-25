# Day 7 학습 일지 — OOP + 콘솔 가계부 + 첫 PR (Week 1 완주!)

**날짜**: 2026-06-17 (화)
**학습자**: 김윤종 (부산)
**특이사항**: 5일 공백 후 복귀 → Week 1 완주! 🎉

---

## 🎯 오늘의 목표 달성도

- [x] day07 환경 준비
- [x] 클래스/객체 개념
- [x] **init** / self
- [x] 던더 메서드 자동 실행 원리
- [x] 메서드 (객체의 행동)
- [x] 콘솔 가계부 (Account 클래스)
- [x] early return
- [x] 메인 메뉴 루프 (가계부 완성)
- [x] if **name** == "**main**"
- [x] Git 복습 + 치트시트 제작
- [x] merge --abort 학습
- [x] 첫 PR 완성! ⭐⭐⭐
- [x] 대시보드 + 역량 로드맵 갱신

---

## 📚 배운 것

### 🐍 OOP (객체지향) — C1·C2

- 발전: 변수 → 딕셔너리 → 클래스(데이터+기능)
- 클래스 = 붕어빵 틀(설계도) / 객체 = 붕어빵(제품)
- "파이썬의 모든 것은 객체" (str/list/dict/파일)
  · .upper()/.append()/.read() = 객체의 메서드였음!
  · type()의 <class '...'>가 그 증거
- class 정의:
  class Person:
  def **init**(self, name): # 생성자(자동 실행)
  self.name = name # 속성
  def introduce(self): # 메서드(행동)
  print(self.name)
- **init**: 객체 생성 시 자동 호출 (초기화)
- self: 객체 자신 (정의엔 쓰고, 호출엔 생략)
- 속성(attribute) = 데이터 / 메서드(method) = 행동
- 객체는 상태 변화를 기억 (살아있다!)

### 🔮 던더(dunder) 메서드

- 양쪽 언더스코어 2개 (**init**, **str**, **len**)
- 파이썬이 특정 순간 자동 호출하기로 "약속"한 메서드
- **init**: 객체 만들 때 / **str**: print할 때 / **len**: len()할 때
- print를 넣어 자동 실행을 눈으로 확인함

### 🐷 콘솔 가계부 (미니 프로젝트)

- Account 클래스: owner/balance/history(속성)
  - deposit/withdraw/show_balance/show_history(메서드)
- 메인 메뉴 루프: while True + if/elif/else + break
- 입력 방어: try/except ValueError
- 일주일 배운 것 총동원 (Day1~7!)

### 🎓 시니어 패턴

- early return(가드 절): 문제 케이스 먼저 차단 → 정상 로직 평평하게
  · return 만나면 그 아래 코드 실행 안 됨
- if **name** == "**main**": 직접 실행 시에만 main() 작동
  · **name**: 직접 실행="**main**" / import=파일명
  · 파일을 "프로그램+재사용 부품" 둘 다로
- 역할 분리: 클래스(데이터·로직) + main(사용자 상호작용)

### 🔀 Git 협업 — C4

- Git 복습: 4영역, add/commit/push, status/log, 브랜치, 충돌
- git merge --abort: 충돌 중(add/commit 전) 병합 취소 → merge 전으로
- git rm: 파일 삭제 + 스테이징 (del과 달리 git에 바로 기록)
- 첫 PR(Pull Request)!
  · PR = "내 브랜치를 main에 합쳐도 될까요?" 정식 요청
  · 흐름: switch -c → push -u → GitHub서 PR 생성 → 병합 → pull
  · Files changed: 초록(+)/빨강(-) = 코드 리뷰 화면
  · @@...@@ = hunk(변경 구역) / 구문강조 = 문법 색칠
  · PR은 브랜치의 거울 → push하면 자동 갱신
  · git pull: GitHub → 내 PC (push의 반대)

---

## 🔗 역량 로드맵 연결

- **C1 AI코딩** (46→52%): OOP로 코드를 객체 단위로 구조화, 관례 체득
- **C2 자료구조** (65→72%): 클래스로 "나만의 자료구조(Account)" 직접 설계
- **C4 Git협업** (45→58%): 첫 PR 전체 사이클 완성 = 협업의 핵심 관문 통과!

---

## 💻 작성한 코드

- learn_object.py (모든 게 객체)
- learn_class.py (클래스 정의)
- learn_init.py (**init** 자동 실행 실험)
- learn_method.py (메서드)
- learn_return.py (early return 실험)
- learn_name.py (**name** 실험)
- budget.py (콘솔 가계부 완성! ⭐)
- git_cheatsheet.md (Git 치트시트)

---

## 🤔 어려웠던 것 / 발견한 것

- self/**init**이 처음엔 낯설었지만, "호출 시 자동 전달" 이해
- 던더 메서드의 "약속" 개념 → print로 자동 실행 직접 확인
- Files changed의 파란색 = hunk 헤더(@@) + 구문강조 (변경과 무관)
- budget.py 교체 → 빨강(-)으로 옛 코드 삭제가 시각적으로 보임
- 5일 공백 후 Git 복습으로 기억 복원 (치트시트로 정리)

---

## 🚀 다음 (Day 8 — Week 2 시작!)

- 상속/다형성 (OOP 2)
- JSON 다루기
- 코드 포매터 (Black/Ruff)

---

## 💭 Week 1 완주 회고

"7일 전엔 변수도 몰랐는데,
지금은 클래스로 객체를 만들고,
예외를 처리하고,
PR로 협업하는 개발자가 되었다.

5일을 쉬었지만 포기하지 않고 돌아왔고,
오히려 복습으로 기초를 더 단단히 했다.

나는 '실험하며 배우는 개발자'다."

---

## 🎯 21일 진척도

- [x] **Week 1 (Day 1~7)**: Python 기초 + Git/GitHub 완주! 🎉
- [ ] Week 2 (Day 8~14): GUI + 비동기 + DB
- [ ] Week 3 (Day 15~21): 시니어 마인드 + 최종 프로젝트
