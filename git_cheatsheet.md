# 🐙 Git 치트시트 (Day 3~6 정리)

> 김윤종 | 21일 Python 학습 | 헷갈릴 때 펼쳐보는 Git 요약집
> GitHub: github.com/AiRoboCop/learning-python-21days

---

## 🗺️ 큰 그림 — Git의 4영역

가장 중요한 지도! 명령어를 외우지 말고 **"파일이 어느 영역에 있나"** 로 이해하기.

```
[작업 공간]  →  [스테이징]  →  [로컬 저장소]  →  [원격 저장소]
Working Dir     Staging         Local Repo        Remote(GitHub)
   │              │                │                  │
   │   git add    │   git commit   │    git push      │
   └─────────────→└───────────────→└─────────────────→
                                    ←─────────────────
                                        git pull
```

| 공간 | 무엇 | 비유 |
|---|---|---|
| 작업 공간 | 지금 편집 중인 파일 | 책상 위 |
| 스테이징 | 커밋할 후보로 올린 것 | 장바구니 |
| 로컬 저장소 | 내 PC에 기록된 버전 | 내 일기장 |
| 원격(GitHub) | 인터넷에 올린 버전 | 클라우드 백업 |

---

## 🚀 시작 (저장소 처음 만들 때, 한 번만)

```powershell
git init                                  # 이 폴더를 Git 저장소로
git config --global user.name "이름"       # 내 정보 (최초 1회)
git config --global user.email "이메일"
git remote add origin <GitHub주소>         # GitHub 연결
git push -u origin main                    # 첫 푸시 (-u: 이후 git push만 쳐도 됨)
```

---

## ⭐ 매일 쓰는 3종 세트

```powershell
git add .                  # 작업공간 → 스테이징 (.은 전부)
git commit -m "메시지"      # 스테이징 → 로컬 저장소 (기록!)
git push                   # 로컬 → GitHub (업로드)
```

> 💡 특정 파일만: `git add 파일명`
> 💡 커밋 메시지는 "무엇을 왜 바꿨는지" 명확하게!

---

## 🔍 상태 확인 (수시로!)

```powershell
git status                 # 현재 상태 — 제일 친한 친구! 막히면 무조건 이것
git log --oneline          # 커밋 기록 (한 줄로 간단히)
git branch                 # 브랜치 목록 (* = 현재 위치)
```

> 🌟 `git status`는 "현재 상태 + 다음에 할 일"을 항상 알려준다.

---

## 📁 .gitignore (Git이 무시할 파일 목록)

프로젝트 폴더에 `.gitignore` 파일을 만들고:

```
.venv/             # 가상환경 (용량 큼, 각자 만들면 됨)
__pycache__/       # 파이썬 캐시
*.log              # 로그 파일
```

---

## 🌿 브랜치 (독립된 작업 공간 = 평행우주)

main을 안전하게 두고, 가지를 쳐서 실험!

```powershell
git branch                 # 브랜치 목록 (* = 현재)
git switch -c 이름         # 생성 + 이동 (-c = create)
git switch 이름            # 이동만
git merge 이름             # 현재 브랜치에 '이름'을 병합
git branch -d 이름         # 삭제 (병합된 것만, 안전)
```

### 브랜치 워크플로우 (전체 흐름)

```
1. git switch -c feature   🌿 가지 만들고 이동
2. 작업 + add + commit      ✍️  거기서 작업
3. git switch main          🏠 본진으로 복귀
4. git merge feature        🔀 작업을 main에 합치기
5. git branch -d feature    🧹 다 쓴 가지 정리
```

> 💡 핵심 원리: **커밋이 파일을 그 브랜치에 "소속"시킨다.**
> - 커밋 전: 모든 브랜치에서 보임 (작업공간 공유)
> - 커밋 후: 그 브랜치에서만 보임 (히스토리에 박제)
> - merge 후: 합친 브랜치에서도 보임 (소속 공유)

---

## ⚡ merge 충돌 (Conflict) 해결

양쪽 브랜치에서 **같은 부분을 다르게 수정**하면 충돌 발생.

### 충돌 마커 모양

```
<<<<<<< HEAD
현재 브랜치 내용
=======
병합하려는 브랜치 내용
>>>>>>> 브랜치명
```

### 해결 3단계

```powershell
# 1. 파일 열어서 마커(<<<, ===, >>>) 편집 → 원하는 내용만 남기기
#    (VS Code: Accept Current / Incoming / Both 버튼 활용)
git add 파일명             # 2. 해결했다고 표시
git commit -m "충돌 해결"   # 3. 병합 완료
```

---

## 🆘 git merge --abort (비상 탈출 버튼)

merge 중 충돌이 났을 때 **병합을 취소하고 merge 직전으로 되돌리기**.

```powershell
git merge --abort          # 충돌 마커 다 사라지고, merge 전 상태로!
```

### 사용 가능 시점 (중요!)

```
git merge 실행
  ↓
⚡ 충돌 발생!
  ↓
┌──────────────────────────────────┐
│ 여기서만 가능! (아직 add/commit 전) │ ← git merge --abort
└──────────────────────────────────┘
  ↓
git add + commit (해결 완료)
  ↓
❌ 완료 후엔 abort 불가
```

> 💡 언제 쓰나: 충돌이 너무 복잡할 때 / 잘못된 브랜치를 merge했을 때 / 그냥 되돌리고 싶을 때
> 💡 "안 되면 abort하면 되지!" → 두려움 없이 merge를 시도할 수 있는 안정감

---

## 🔠 헷갈리기 쉬운 것 — 대문자 = 강제(force)!

```
git branch -d 이름   →  안전 삭제 (병합된 것만)
git branch -D 이름   →  강제 삭제 (대문자!)

git branch -m 이름   →  안전 이름변경
git branch -M 이름   →  강제 이름변경 (대문자!)
```

> ⚠️ 대문자(강제)는 강력하지만 되돌리기 어려울 수 있으니 신중하게!

---

## 🎯 한눈에 보는 전체 치트시트

```
═══ 시작 (1회) ═══
git init                     저장소 만들기
git remote add origin URL    GitHub 연결
git push -u origin main      첫 푸시

═══ 매일 (3종 세트) ═══
git add .                    스테이징
git commit -m "메시지"        기록
git push                     GitHub 업로드

═══ 확인 ═══
git status                   현재 상태 (제일 친한 친구!)
git log --oneline            커밋 기록
git branch                   브랜치 목록

═══ 브랜치 ═══
git switch -c 이름           생성 + 이동
git switch 이름              이동
git merge 이름               병합
git branch -d 이름           삭제

═══ 충돌 ═══
마커 편집 → git add → git commit    해결
git merge --abort                    취소(해결 전에만)
```

---

## 🌟 기억할 한 가지

> **Git은 명령어를 암기하는 게 아니라, "지금 파일이 어느 영역에 있나"를 이해하는 것.**
> 4영역 그림(작업 → 스테이징 → 로컬 → 원격)만 머릿속에 있으면 모든 명령어가 자연스럽게 연결된다.

---

*— Day 3~6 학습 정리 | 다음: PR(Pull Request), rebase/squash 머지 (Phase 2)*
