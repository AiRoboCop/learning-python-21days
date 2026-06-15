text = "hello"
numbers = [1,2,3]
info = {"name" : "윤종"}

print("=== 이미 객체였다! ===")

print(type(text))
print(type(numbers))
print(type(info))

print()
print("=== 객체의 메서드 ===")
print(text.upper())

print(numbers)
numbers.append(4)
print(numbers)