is_sunny = True
is_raining = False

print(f"오늘 맑음? {is_sunny}")
print(f"오늘 비? {is_raining}")
print(f"is_sunny의 타입{type(is_sunny)}")

print("=== Truthy & Falsy 확인 ===")
print(f"bool(0) = {bool(0)}")              # False
print(f"bool(1) = {bool(1)}")              # True
print(f"bool(-1) = {bool(-1)}")            # True (음수도!)
print(f"bool('') = {bool('')}")            # False (빈 문자열)
print(f"bool(' ') = {bool(' ')}")          # True (공백 한 칸!)
print(f"bool('hello') = {bool('hello')}")  # True
print(f"bool([]) = {bool([])}")            # False (빈 리스트)
print(f"bool([0]) = {bool([0])}")          # True (요소가 있으니까!)
print(f"bool(None) = {bool(None)}")        # False