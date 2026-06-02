

total = 0

for i in range(1, 11):
    total += i

print(f"1 에서 10 까지의 합 : {total}")

print()
dan = int(input("몇 단을 출력할까요?"))

print(f"=== {dan} ===")

for i in range(1, 10):
    print(f"{dan} * {i} = {dan * i}")

print()
print("=== range(5) ===")

for i in range(5):
    print(f"반복 {i}번째")

print()
print("=== range(1, 6) ===")
for i in range(1, 6):
    print(f"숫자: {i}")