# 계산 도구 모듈
# calculator.py

# 더하기
def add(a : float, b : float) -> float:
    """덧셈"""
    return a + b

# 빼기
def subtract(a : float, b : float) -> float:
    """뺄셈"""
    return a - b

# 곱하기
def multiply(a : float, b : float) -> float:
    """곱셈"""
    return a * b

# 나누기
def divide(a : float, b : float) -> float:
    """나눗셈"""
    return a / b

if __name__ == "__main__":
    print("=== 모듈 자체 테스트 ===")
    print(f"add(2, 3) = {add(2,3)}")
    print(f"subtract(2, 3) = {subtract(2,3)}")
    print(f"multiply(2, 3) = {multiply(2,3)}")
    print(f"divide(2, 3) = {divide(2,3)}")