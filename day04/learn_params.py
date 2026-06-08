def make_profile(name : str, age : int, city : str) -> None:
    """프로필 출력"""
    print(f"{name} / {age}세 / {city}")

print("=== 위치 인자 ===")
make_profile("윤종", 30, "부산")

print("=== 키워드 인자 (순서 무관) ===")
make_profile(name="윤종", city="부산", age="30")

def greeting(name : str, greeting : str = "안녕하세요") -> None:
    """인사 출력(greeting 기본값 있음)"""
    print(f"{greeting}, {name}님")

print()
print("=== 기본값 매게변수 ===")
greeting("윤종")
greeting("윤종", "반갑습니다.")

def min_and_max(numbers : list) -> tuple:
    """리스트의 최속값과 최댓값을 함께 반환"""
    return min(numbers), max(numbers)

print()
low, high = min_and_max([3,1,2,3,4,5])
print(f"최소:{low}, 최대:{high}")