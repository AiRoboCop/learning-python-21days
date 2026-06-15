class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

yunjong = Person("김윤종", 50, "부산")
younghee = Person("이영희", 30, "서울")

print(f"{yunjong.name}, {yunjong.age}, {yunjong.city}")
print(f"{younghee.name}, {younghee.age}, {younghee.city}")

print()
print(f"yunjong의 도시 : {yunjong.city}")
print(f"younghee의 도시 : {younghee.city}")

print()
print(type(yunjong))
print(type(yunjong).__name__)