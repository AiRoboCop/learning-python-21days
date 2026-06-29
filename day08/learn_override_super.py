# 오버라이딩 vs 오버라이딩 + super() 비교

class Animal:
    def greet(self):
        print("나는 동물이에요")

# 경우 1 : 오버라이딩 만(super 없음)
class Dog(Animal):
    def greet(self):
        print("멍멍! 나는 개에요")

# 경우 2 : 오버라이딩 + super()
class Cat(Animal):
    def greet(self):
        super().greet()
        print("야옹! 나는 고양이에요")

print("super() 없음")        
dog = Dog()
dog.greet()

print("super() 있음")        
cat = Cat()
cat.greet()