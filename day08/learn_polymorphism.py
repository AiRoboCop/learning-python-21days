# 다형성(polymorphism)

class Animal:
    def __init__(self, name:str) -> None:
        self.name = name

    def sound(self):
        print(f"{self.name}: (소리 없음)")

class Dog(Animal):
    def sound(self):
        print(f"{self.name}: 명명")

class Cat(Animal):
    def sound(self):
        print(f"{self.name}: 야옹")

class Cow(Animal):
    def sound(self):
        print(f"{self.name}: 음메")

# 여러동물을 리스트에 담기
animal_list = [Dog("강아지"), Cat("고양이"), Cow("송아지")]

for n in animal_list:
    n.sound()