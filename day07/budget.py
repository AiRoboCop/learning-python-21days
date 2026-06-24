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



# 입금/출금/조회/내역/종료