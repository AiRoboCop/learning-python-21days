# 콘솔 가계부 - Account 클래스
# 입금/출금/조회/내역/종료
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
# acc = Account("김윤종")
# acc.deposit(10000)
# acc.withdraw(3000)
# acc.withdraw(50000) #잔액 부족 테스트
# acc.show_balance()
# acc.show_history()

def main():
    """가계부 메인 프로그램"""
    owner = input("계좌 주인 이름을 입력하세요")
    account = Account(owner)
    print(f"\n {owner}님의 가계부를 시작합니다.\n")

    while True:
        #메뉴 출력
        print("=" * 30)
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액 조회")
        print("4. 거래 내역")
        print("5. 종료")
        print("=" * 30)

        choice = input("선택 (1~5):")

        if choice == "1":   # 입금
            try:
                amount = int(input("입금할 금액 : "))
                account.deposit(amount)
            except ValueError:
                print("숫자만 입력하세요")

        elif choice == "2": # 출금
            try:
                amount = int(input("출금할 금액 : "))
                account.withdraw(amount)
            except ValueError:
                print("숫자만 입력하세요")

        elif choice == "3": # 잔액 조회
            account.show_balance()
        
        elif choice == "4": # 거래 내역
            account.show_history()
        
        elif choice == "5": # 종료
            print(f"\n{owner}님, 가계부를 종료합니다. 안녕히 가세요!")
            break

        else:
            print("1-5 중에서 선택하세요")

        print()

# 프로그램 시작!
if __name__ == "__main__":
    main()