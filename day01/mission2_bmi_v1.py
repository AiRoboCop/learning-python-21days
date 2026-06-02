# 미션 2 — BMI 계산기 (난이도: 보통)
# === BMI 계산기 ===
# 이름이 뭐예요? 김윤종
# 키를 cm 단위로 입력하세요: 175
# 몸무게를 kg 단위로 입력하세요: 70

# ------------------------------
# 김윤종님의 BMI 결과
# ------------------------------
# 키: 175cm (1.75m)
# 몸무게: 70kg
# BMI: 22.86
# ------------------------------

def get_user_info() -> dict:
    """ 사용자 정보 수집 및 BMI 수치 계산 """
    name = input("이름이 뭐예요? ")
    height_cm = float(input("키를 cm 단위로 입력하세요: "))
    weight = float(input("몸무게를 kg 단위로 입력하세요: "))

    height_m = height_cm / 100
    bmi = weight / (height_m * 2)

    return {
        "name" : name,
        "height_cm" : height_cm,
        "height_m" : height_m,
        "weight" : weight,
        "bmi" : bmi
    }

def print_introduction(user : dict) -> None:
    """ Dict 형태로 받은 값을 출력 """
    print("-" * 30)
    print(f"{user["name"]}님의 BMI 결과")
    print("-" * 30)

    print(f"키: {user["height_cm"]}cm ({user["height_m"]}m)")
    print(f"몸무게: {user["weight"]}kg")
    print(f"BMI: {user["bmi"]:.2f}")

    print("-" * 30)

def main() -> None:
    user = get_user_info()
    print_introduction(user)

if __name__ == "__main__":
    main()