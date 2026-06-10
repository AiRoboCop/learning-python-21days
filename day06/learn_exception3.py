def safe_divide(a_str : str, b_str : str) -> None:
    """문자열 두 개를 받아 나눗셈 (안전하게)"""
    try:
        a = int(a_str)
        b = int(b_str)
        result = a / b
    except ValueError:
        print("숫자를 입력하세요!")
    except ZeroDivisionError:
        print("0으로 나눌 수 없어요!")
    else:
        print(f"결과 : {result}")
    finally:
        print("--- 계산 시도 완료 ---")

print("=== 정상 케이스 ===")
safe_divide("10", "2")

print()
print("=== 0으로 나누기 ===")
safe_divide("10", "0")

print()
print("=== 잘못된 입력 ===")
safe_divide("abc", "2")