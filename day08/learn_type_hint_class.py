# 클래스 메서드의 타입 힌트

class Account:
    def __init__(self, owner:str) -> None:
        self.owner : str = owner
        self.balance : int = 0

    def deposit(self, amount:int) -> None:
        """입금(반환값 없음 -> None)"""
        self.balance += amount
        print(f"{amount}원 입금. 잔액 : {self.balance}원")

    def get_balance(self) -> int:
        return self.balance
    
acc = Account("김윤종")
acc.deposit(10000)
current = acc.get_balance()
print(f"현재 잔액 : {current}원")
