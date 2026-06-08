
print(True or (1/0))
print()

print("안전한 나눗셈")

x = 0
result = x != 0 and 1/x > 0.5
print(f"x = {x}, 안전검사 1:{result}")

x = 4
result = x != 0 and 1/x > 0.5
print(f"x = {x}, 안전검사 2:{result}")

x = 1
result = x != 0 and 1/x > 0.5
print(f"x = {x}, 안전검사 3:{result}")


age = 19
print(f"20대인가? {age >= 20 and age < 30}")
print(f"미성년자거나 노인인가? {age <= 19 or age >= 65}")
print()
print(f"20대인가? {20 <= age < 30}")
print(f"미성년자거나 노인인가? {19 >= age >= 65}")


print("=== 성인 + 한국 거주자 확인 ===")

age = 30
country = "한국"

is_adult = age > 19
is_korean = country == "한국"

print(f"나이 {age}세, 거주국 {country}")
print(f"성인인가? {is_adult}")
print(f"한국 거주자인가? {is_korean}")
print(f"성인 AND 한국 거주자? {is_adult and is_korean}")
print(f"성인 OR 한국 거주자? {is_adult or is_korean}")
print(f"성인이 아닌가? {not is_adult}")


# 1) and: 둘 다 True 일 때만 True
# print("=== and (그리고) ===")
# print(f"True and True   = {True and True}")    # True
# print(f"True and False  = {True and False}")   # False
# print(f"False and True  = {False and True}")   # False
# print(f"False and False = {False and False}")  # False

# 2) or: 하나라도 True면 True
# print()
# print("=== or (또는) ===")
# print(f"True or True   = {True or True}")      # True
# print(f"True or False  = {True or False}")     # True
# print(f"False or True  = {False or True}")     # True
# print(f"False or False = {False or False}")    # False

# 3) not: 뒤집기
# print()
# print("=== not (아니다) ===")
# print(f"not True  = {not True}")               # False
# print(f"not False = {not False}")              # True