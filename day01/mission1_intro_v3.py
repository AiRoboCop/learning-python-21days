# 미션 1 — 자기소개 프로그램 (난이도: 쉬움)

# 정보 수집 함수
def get_user_info():
    name = input("이름이 뭐예요? ")
    age = int(input("나이가 몇이에요? "))
    city = input("어디 사세요? ")
    favorite_food = input("좋아하는 음식은? ")

    return {
        "name" : name,
        "age" : age,
        "city" : city,
        "favorite_food" : favorite_food,
    }

# 정보 출력 함수
def print_introduction(user):
    """입력받은 user 딕셔너리를 바탕으로 자기소개 출력"""

    print("-" * 30)
    print(f"안녕하세요! 저는 {user['name']}입니다.")
    print(f"{user['age']}살이고, {user['city']}에 살아요.")
    print(f"제가 가장 좋아하는 음식은 {user['favorite_food']}예요!")
    print(f"내년이면 {user['age'] + 1}살이 됩니다.")
    print("-" * 30)

user_info = get_user_info()
print_introduction(user_info)

# print(f"이 파일의 name은 {__name__} 입니다.")