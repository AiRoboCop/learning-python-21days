# Day 4 학습 일지 — 함수 심화 + 모듈 + GitHub

**날짜**: 2026-05-29 (금)
**학습자**: 김윤종 (부산)
**컨디션**: [기록]
**학습 시간**: [기록]

---

## 🎯 오늘의 목표 달성도

- [x] day04 환경 준비
- [x] 함수 매개변수 심화 (위치/키워드 인자)
- [x] 기본값 매개변수
- [x] 여러 값 반환 (언패킹 맛보기)
- [x] 스코프 (지역 변수 vs 전역 변수)
- [x] 모듈 만들기 (계산기 모듈)
- [x] 메인 가드 실전 확인 ⭐
- [x] GitHub 계정 + 원격 저장소
- [x] git push (코드 공개!) 🌐
- [x] Git 4영역 전체 이해

---

## 📚 배운 것

### 🐍 Python

- 위치 인자 vs 키워드 인자 (func(name="윤종"))
- 키워드 인자: 순서 무관, 가독성 ↑
- 기본값 매개변수: def greet(name, greeting="안녕하세요")
- 기본값 있는 매개변수는 뒤쪽에!
- 여러 값 반환: return min(x), max(x)
- 언패킹: low, high = func()
- min(), max() 내장 함수
- 스코프: 변수가 살아있는 범위
- 지역 변수: 함수 안에서만 (NameError)
- 전역 변수: 어디서나 읽기 가능
- 함수 안 전역 변수 수정 → UnboundLocalError
- global보다 매개변수+반환이 안전 (순수 함수!)
- 모듈: 함수/변수를 담은 .py 파일
- import calculator → calculator.add()
- from calculator import add → add()
- 메인 가드: import 시 테스트 코드 실행 안 됨 (실전 확인!)

### 🔀 Git / GitHub (오늘의 하이라이트!)

- Git = 버전 관리 도구 (내 PC)
- GitHub = 클라우드 서비스 (인터넷)
- Git 4영역:
  ① Working Directory (작업 공간)
  ② Staging Area (스테이징)
  ③ Local Repository (로컬 저장소)
  ④ Remote · GitHub (원격)
- 명령어 = 영역 간 이동:
  git add: ①→②
  git commit: ②→③
  git push: ③→④
  git pull: ④→③
  git clone: ④→새 폴더
- 상태 확인: status(①②), log(③), remote -v(④)
- git remote add origin <URL>: 원격 연결
- git push -u origin main: 첫 push
- 다른 PC 작업: clone → 작업 → push / pull로 동기화

### 💻 CLI

- 파이프 | : 명령 결과를 다음 명령으로 전달
- 리다이렉션 > : 결과를 파일로 저장 (덮어쓰기)
- 리다이렉션 >> : 파일 끝에 추가

### 🌟 시니어 사고법

- 인자 3개 이상이면 키워드 인자가 안전
- 자주 쓰는 값은 기본값, 가끔 바꿀 값은 키워드 인자
- "함수는 섬처럼 독립적으로" (순수 함수)
- 전역 변수는 최소화 (디버깅 지옥 방지)
- 768줄 = 여러 모듈의 협업 (database.py, excel.py, ui.py)
- GitHub = 개발자의 이력서 (잔디, 프로젝트)
- Git 명령어는 "영역 간 이동"으로 이해

---

## 💻 작성한 코드

### calculator.py (첫 모듈!)

```python
def add(a: float, b: float) -> float:
    """덧셈"""
    return a + b
# subtract, multiply, divide...

if __name__ == "__main__":
    print(f"add(2, 3) = {add(2, 3)}")
```

### main_calc.py (모듈 가져다 쓰기)

```python
import calculator

def main() -> None:
    print(f"10 + 3 = {calculator.add(10, 3)}")

if __name__ == "__main__":
    main()
```

---

## 🤔 어려웠던 것 / 발견한 것

### 발견 1: 메인 가드의 진짜 의미

- calculator를 import해도 테스트 코드가 안 나옴
- "직접 실행할 때만 테스트, 가져다 쓸 땐 함수만"
- Day 1 이론 → Day 4 실전으로 연결!

### 발견 2: 커밋 안 하면 push도 안 됨

- 커밋 안 한 파일은 GitHub에 안 올라감
- 스스로 add → commit → push로 해결
- Git 4영역으로 이유 이해

### 발견 3: Git 전체 그림

- 명령어 외우기 → 전체 지도 이해로 전환
- "지금 내 코드가 어느 영역에 있나" 파악 가능

---

## 🚀 내일 할 것 (Day 5)

- 리스트 (list): 여러 값을 순서대로 담기
- 딕셔너리 (dict): 키-값 쌍으로 담기
- 튜플 (tuple), 세트 (set)
- 파일 입출력 (파일 읽고 쓰기)
- VS Code 디버거 (중단점, 한 줄씩 실행)
- → 대시보드 데이터를 직접 수정할 수 있게 됨!

---

## 💭 오늘의 한 줄 회고

"함수를 나눠 담는 법(모듈)을 배웠고,
코드를 세상에 공개(GitHub)했으며,
Git이라는 도구의 전체 지도를 손에 넣었다.
이제 명령어를 외우지 않고, 이해한다."

---

## 🎯 21일 진척도

- [x] **Day 1**: 환경 + 변수/입출력 ✅
- [x] **Day 2**: 자료형, 조건문 ✅
- [x] **Day 3**: 반복문, 게임, Git 입문 ✅
- [x] **Day 4**: 함수 심화, 모듈, GitHub ✅
- [ ] Day 5: 자료구조 (리스트/딕셔너리) + 파일 I/O
- [ ] Day 6~7: 예외 처리 + OOP + 미니 프로젝트
- [ ] Day 8~14: GUI + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
