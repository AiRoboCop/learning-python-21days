# Day 8 학습 일지 — 상속·다형성(OOP 2) + JSON + 코드 포매터

**날짜**: 2026-06-18 (수)
**학습자**: 김윤종 (부산)
**특징**: 질문 폭발의 날! (개념을 사방으로 확장)

---

## 🎯 오늘의 목표 달성도

- [x] day08 환경 준비
- [x] 상속 (Inheritance)
- [x] 메서드 찾기 순서 (자식→부모)
- [x] 다단계 상속 / 다중 상속
- [x] 오버라이딩 + super()
- [x] 다형성 (Polymorphism)
- [x] 클래스 타입 힌트
- [x] 생성자 상속 + 인자 규칙
- [x] JSON (dump/load)
- [x] 파일 I/O vs JSON 비교
- [x] Black / Ruff 코드 포매터 (자동 설정!)
- [x] 대시보드 + 역량 로드맵 갱신

---

## 📚 배운 것

### 🐍 상속 (Inheritance) — C1·C2

- class 자식(부모): → 부모의 속성·메서드 물려받기
- 부모=슈퍼/기반 클래스, 자식=서브/파생 클래스
- 메서드 찾기: 자식 → 부모 순서로 올라가며 탐색
- 다단계 상속: 할아버지→부모→자식 (계속 위로 탐색)
- 다중 상속: class 자식(부모1, 부모2) → 왼쪽 우선(MRO)
- "is-a 관계"일 때 상속 (Dog is a Animal)
- 실무: 상속은 얕고 명확하게! (깊은/복잡한 상속 피하기)

### 🔧 오버라이딩 + super()

- 오버라이딩: 물려받은 메서드를 자식이 같은 이름으로 재정의 (덮어쓰기)
- super(): 오버라이딩 안에서 부모 메서드 호출
  · super() 없이 → 부모 완전 대체
  · super() 있이 → 부모 + 자식 추가
- super().**init**(): 부모 초기화 호출 (속성 설정)

### 🧬 다형성 (Polymorphism)

- "하나의 명령(메서드 이름), 여러 모습(동작)"
- 같은 sound() 호출 → 객체마다 다르게 (Dog 멍멍, Cat 야옹)
- 상속 + 오버라이딩의 결과
- 하나의 반복문으로 여러 객체 처리!
- OCP(개방-폐쇄): 새 타입 추가해도 기존 코드 안 고침

### 📦 클래스 심화

- 메서드 타입 힌트: 함수와 동일 (self엔 안 붙임)
- 속성 타입 힌트: self.balance: int
- 내 클래스 타입: target: "Account" (따옴표=전방참조)
- 생성자 상속: 자식에 **init** 없으면 부모 것 자동 사용
- 생성자 인자: 실행되는 생성자가 요구하면 필수
  · 기본값 없으면 필수, 있으면 선택 (함수와 동일)
- 일회용 객체: Cat().greet() → 변수에 안 담고 바로 사용

### 💾 JSON — C2 (→ C3 다리)

- JSON ≈ 파이썬 딕셔너리 (거의 같은 모습)
- import json (기본 내장)
- json.dump(데이터, f): dict → 파일 (저장, "쏟아붓다")
- json.load(f): 파일 → dict (불러오기)
- ensure_ascii=False: 한글 안 깨짐 / indent=2: 보기 좋게
- json.dumps/loads: 문자열 버전 (s=string)
- 영속성(persistence): 데이터 저장하고 불러오기

### 🆚 파일 I/O vs JSON

- 파일 I/O: 텍스트(문자열) 그대로 (f.write/read)
- JSON: 데이터 구조 저장, 타입·구조 보존 (dump/load)
- 읽을 때: 파일I/O는 전부 문자열 / JSON은 타입 유지
- write(문자열 그대로) vs dump(변환 후 쓰기)
- JSON은 파일 I/O 위에 "변환 기능"을 얹은 것
- 단순 글→파일I/O, 구조화 데이터→JSON

### 🎨 코드 포매터 — C1

- Black: 코드 "모양" 정리 (띄어쓰기, 따옴표, 들여쓰기)
- Ruff: 코드 "문제" 검사 (안 쓰는 import/변수)
- pip install black ruff
- black 파일.py / ruff check 파일.py / ruff check --fix
- VS Code: Black Formatter 확장 + Format On Save
  · settings.json에 defaultFormatter + formatOnSave
  · "설정 ≠ 설치" (확장도 설치해야 작동!)

---

## 🔗 역량 로드맵 연결

- **C1 AI코딩** (52→57%): OOP 2로 코드 구조화 + Black/Ruff 자동 포매팅 환경
- **C2 자료구조** (72→78%): 상속·다형성으로 클래스 계층 설계 + JSON 데이터 저장/교환 → DB(C3)로 가는 다리

---

## 💻 작성한 코드

- learn_inherit.py (상속)
- learn_lookup.py (메서드 찾기)
- learn_multi_inherit.py (다단계 상속)
- learn_multiple.py (다중 상속)
- learn_super.py (오버라이딩+super, SavingsAccount!)
- learn_override_super.py (super 비교)
- learn_polymorphism.py (다형성)
- learn_type_hint_class.py (클래스 타입 힌트)
- learn_inherit_init.py (생성자 상속)
- learn_init_args.py (생성자 인자)
- learn_json.py (JSON, account.json 생성!)
- messy.py (Black 포매팅 실습)
- check.py (Ruff 검사 실습)

---

## 🤔 오늘의 질문들 (사방으로 확장!)

- 여러 단계 상속? → 다단계 (계속 위로 탐색)
- 여러 부모? → 다중 상속 (왼쪽 우선)
- 클래스에 타입 힌트? → 가능 (self 빼고)
- 객체 바로 쓰기? → 일회용 객체 (변수에 안 담음)
- 생성자도 물려받나? → 자식에 없으면 부모 것
- 물려받으면 인자 필수? → 실행되는 생성자 기준
- 파일I/O vs JSON? → 텍스트 vs 데이터 구조
- write vs dump? → 그대로 vs 변환

---

## 🚀 다음 (Day 9)

- tkinter GUI 시작! (드디어 화면이 있는 프로그램!)
- 커밋 컨벤션 (좋은 커밋 메시지 작성법)

---

## 💭 오늘의 한 줄 회고

"설명을 듣고 멈추지 않고,
'그럼 이건?' '저건?' 하고 계속 물으며
OOP를 사방으로 확장해 이해했다.
질문이 곧 학습이다."

---

## 🎯 21일 진척도

- [x] **Week 1 (Day 1~7)**: Python 기초 + Git/GitHub
- [x] **Day 8**: OOP 2 + JSON + 코드 포매터 ✅
- [ ] Day 9~14: GUI + 비동기 + DB
- [ ] Day 15~21: 시니어 마인드 + 최종 프로젝트
