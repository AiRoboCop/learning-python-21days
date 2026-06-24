# 콘솔 가계부 - Account 클래스
# 속성 : owner(소유자), balance(잔액), history(거래내역)
# 메서드
#   - deposit(입금)
#   - withdraw(출금) - 잔액 부족 체크!
#   - show_balance(잔액 조회)
#   - show_history(거래 내역)
class Account:
    def __init__(self, owner):
        self.owner = owner  # 소유자 (속석)
        self.balance = 0    # 잔액, 처음엔 0원(속성)
        self.history = []   # 거래 내역, 빈 리스트(속성)

    def deposit(self, amount):
        """입금 메서드"""
        self.balance += amount
        self.history.append(f"입금: +{amount}원")
        print(f"{amount}원 입금 완료. 잔액: {self.balance}원")

    def withdraw(self, amount):
        """출금 메서드(잔액 부족 체크!)"""
        if amount > self.balance:
            print(f"잔액 부족 (현재 잔액: {self.balance}원)")
            return

        self.balance -= amount
        self.history.append(f"출금: -{amount}원")
        print(f"{amount}원 출금 완료. 잔액: {self.balance}원")

    def show_balance(self):
        """잔액 조회 메서드"""
        print(f"{self.owner}님의 잔액은 {self.balance}원 입니다.")

    def show_history(self):
        """거래 내역"""
        print(f"{self.owner}님의 거래 내역:")
        if not self.history:
            print("(거래 없음)")
        for record in self.history:
            print(f"- {record}")

# === 테스트 ===
acc = Account("김윤종")
acc.deposit(10000)
acc.withdraw(3000)
acc.withdraw(50000) #잔액 부족 테스트
acc.show_balance()
acc.show_history()



# 입금/출금/조회/내역/종료