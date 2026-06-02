
print("=== 비밀번호 맞추기 ===")

while True:
    answer = input("비밀번호?")

    if answer == "1234":
        print("정답")
        break
    
    print("틀렸어요")


print()

print("=== continue : 홀수만 ===")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"홀수 : {i}")

print("반복 종료")

print()

print("=== break : 5에서 멈춤 ===")

for i in range(1, 6):
    if i == 5:
        print("5발견! 멈춥니다.")
        break
    print(f"숫자: {i}")

print("반복 종료")