
print(f"0.2 + 0.2 = {0.2 + 0.2}")

age = 30

is_adult = age >= 19
print(f"어른이 맞나요? {is_adult}")

is_oldman = age >= 60
print(f"어르신이 맞나요? {is_oldman}")

if 20 <= age < 30:
    print("20대 O")
else:
    print("20대 X")

print(f"20 <= age < 30 : {20 <= age < 30}")
print(f"30 <= age < 40 : {30 <= age < 40}")

answer = input("계속? (Y/N): ").upper()
if answer == "Y":
    print("계속합니다.")
else:
    print("stop")

name = "윤종"
print()
print("=== 문자열 비교 ===")
print(f"name == '윤종': {name == '윤종'}")    # True
print(f"name == '상현': {name == '상현'}")    # False
print(f"name != '상현': {name != '상현'}")    # True

age = 30

print(f"age == 30: {age == 30}")
print(f"age == 25: {age == 25}")

print(f"age != 30: {age != 30}")
print(f"age != 25: {age != 25}")

print(f"age > 20: {age > 20}")
print(f"age < 20: {age < 20}")

print(f"age >= 30: {age >= 30}")
print(f"age <= 29: {age <= 29}")