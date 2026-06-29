# JSON 다루기

import json # JSON 모듈(파이썬 기본 내장)

# 1) 저장할 데이터
account_data = {
    "owner" : "김윤종",
    "balance" : 10000,
    "history" : ["입금: +10000원", "출금: -3000원"],
}

# 2) JSON 파일로 저장 (dict → 파일)
with open("account.json", "w", encoding="utf-8") as f:
    json.dump(account_data, f, ensure_ascii=False, indent=2)
print("account.json 파일로 저장 완료")

# 3) JSON 파일에서 불러오기 (파일 → dict)
with open("account.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("파일에서 불러오기 완료!")

# 4) 불러온 데이터 사용
print(f"소유자: {loaded_data['owner']}")
print(f"잔액: {loaded_data['balance']}")
print(f"거래 내역: {loaded_data['history']}")