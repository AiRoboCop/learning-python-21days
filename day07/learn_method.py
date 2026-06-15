class test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intrudece(self):
        print(f"나는 {self.name} 입니다, {self.age} 살 입니다.")

    def brithday(self):
        self.age += 1
        print(f"{self.age} 살 생일을 축하합니다.")

kim = test("김윤종", 50)

kim.intrudece()
kim.brithday()
print(f"생일이 지나고 {kim.name}님의 나이는 {kim.age}")
print()


print()
lee = test("이소령", 30)
lee.intrudece()
kim.intrudece()