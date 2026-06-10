print("=== 정상 케이스 ===")

try:
    number = int("123")
    print(f"변환성공 : {number}")
except ValueError:
    print("숫자가 아니에요!")

print()
print("=== 에러 발생 ===")
try:
    number = int("abc")
    print(f"변환성공 : {number}")
except ValueError as e:
    print(f"숫자가 아니에요! (에러를 잡았어요)\n{e}")

print()
print("=== 에러 메시지 ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"에러 내용 : {e}")


print()
print("=== 에러 메시지 모를때 ===")
try:
    result = 10 / 0
except Exception as e:
    print(f"에러 내용 : {e}")
    print(f"에러 종류 {type(e)}")
    print(f"에러 종류 {type(e).__name__}")


print()
print("=== 숫자 입력 오류 방지 ===")

try:
    user_num = int(input("숫자를 입력하세요!"))
    print(f"입력한 숫자는 {user_num} 입니다.")
except ValueError:
    print("숫자만 입력해주세요!")