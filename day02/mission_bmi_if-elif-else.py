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

def calculate_bmi(weight_kg : float, height_m : float) -> float:
    """bmi 수치 계산"""
    
    return weight_kg / (height_m ** 2)

def get_bmi_grade(bmi : float) -> str:
    
    if bmi < 18.5:
        return '18.5 미만: "저체중" '
    elif 18.5 <= bmi < 23:
        return '18.5 이상 23 미만: "정상 체중"'
    elif 23 <= bmi < 25:
        return '23 이상 25 미만: "과체중"'
    else:
        return '25 이상: "비만"'

def get_user_info() -> dict:
    """ 사용자 정보 수집 """
    
    name = input("이름이 뭐예요? ")
    height_cm = float(input("키를 cm 단위로 입력하세요: "))
    weight_kg = float(input("몸무게를 kg 단위로 입력하세요: "))

    return {
        "name" : name,
        "height_cm" : height_cm,
        "weight_kg" : weight_kg
    }

def print_introduction(user : dict) -> None:
    """ Dict 형태로 받은 값을 출력 """

    name = user["name"]
    height_cm = user["height_cm"]
    weight_kg = user["weight_kg"]

    height_m = height_cm / 100
    bmi = calculate_bmi(weight_kg, height_m)
    bmi_msg = get_bmi_grade(bmi)

    print("-" * 30)
    print(f"{name}님의 BMI 결과")
    print("-" * 30)

    print(f"키: {int(height_cm)}cm ({height_m:.2f}m)")
    print(f"몸무게: {weight_kg}kg")
    print(f"BMI: {bmi:.2f}")
    print(bmi_msg)

    print("-" * 30)

def main() -> None:
    user = get_user_info()
    print_introduction(user)

if __name__ == "__main__":
    main()