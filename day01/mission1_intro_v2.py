# 미션 1 — 자기소개 프로그램 (난이도: 쉬움)

# 정보 수집
name = input("이름이 뭐예요? ")
age = int(input("나이가 몇이에요? "))
city = input("어디 사세요? ")
favorite_food = input("좋아하는 음식은? ")

# 정보 출력

print("-" * 30)
print(f"안녕하세요! 저는 {name}입니다.")
print(f"{age}살이고, {city}에 살아요.")
print(f"제가 가장 좋아하는 음식은 {favorite_food}예요!")
print(f"내년이면 {age + 1}살이 됩니다.")
print("-" * 30)