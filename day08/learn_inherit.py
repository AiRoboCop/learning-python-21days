# 상송 (Inheritance)

class Animal:
    """부모 클래스"""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}가 밥을 먹어요.")

    def sleep(self):
        print(f"{self.name}가 잠을 자요")        

class Dog(Animal):
    """자식 클래스 - Animal을 물려받음!"""
    def bark(self):
        print(f"{self.name}가 멍멍! 짖어요.")


#객체 만들기
my_dog = Dog("바둑이")

#물려받은 메서드(Animal 것)
my_dog.eat()
my_dog.sleep()

#자기만의 메서드
my_dog.bark()