person = {
    "name" : "윤종",
    "city" : "부산",
    "language" : "Python",
}

print(f"전체 {person}")

print()

print(f"이름 : {person["name"]}")
print(f"도시 : {person["city"]}")

print()

person["job"] = "개발자"
person["language"] = "Python, SQL"

print(f"변경후 : {person}")

print()

for key, val in person.items():
    print(f" {key} : {val}")

print()

employees = [
    {"name" : "김철수", "dept" : "영업"},
    {"name" : "이영희", "dept" : "개발"},
    {"name" : "박민수", "dept" : "인사"},
]

for emp in employees:
    print(f"{emp['name']} = {emp['dept']} 팀")

print()
print(f"{employees[0]}")

print()
print(f"{employees[0]["name"]}")
print(f"{employees[0]["dept"]}")