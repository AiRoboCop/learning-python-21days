# 오버라이딩 + super() - 저축 계좌 만들기

class Account:
    """어제 만든 계좌 (보모)"""
    def __init__(self, owner:str) -> None:
        self.owner = owner
        self.balance = 0
    
    def deposit(self, amount:int) -> None:
        self.balance += amount
        print(f"{amount}원 입금. 잔액:{self.balance}원")

class SavingsAccount(Account):
    """저축 계좌(자식) - Account를 물려받음"""

    def __init__(self, owner:str, rate:float):
        super().__init__(owner)
        self.rate = rate

    def add_interest(self) -> None:
        interest = int(self.balance * self.rate)
        self.balance += interest
        print(f"이자 {interest}원 추가 : 잔액 {self.balance}원")

saving = SavingsAccount("김윤종",0.1)
saving.deposit(10000)
print(f"{saving.owner}님의 잔액 : {saving.balance}원")

print("이자 추가")
saving.add_interest()
print(f"{saving.owner}님의 이자율 : {saving.rate}%")
print(f"{saving.owner}님의 잔액 : {saving.balance}원")