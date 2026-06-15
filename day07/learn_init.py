class Person:
    def __init__(self, name):
        print(f"🐣 __init__ 실행됨! (name={name})")
        self.name = name

print("--- 1. 객체 만들기 전 ---")
yunjong = Person("김윤종")      # 여기서 __init__ 자동 실행!
print("--- 2. yunjong 생성 완료 ---")
younghee = Person("이영희")     # 또 자동 실행!
print("--- 3. younghee 생성 완료 ---")        