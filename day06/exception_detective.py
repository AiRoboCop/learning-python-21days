# 예외 탐정 - 정체 밝히기

print("=== 사건 1 ===")
person = {"name" : "김윤종"}
try:
    print(person["age"])
# except Exception as e:
#     print(f"에러내용 : {e}")
#     print(f"에러명칭 : {type(e).__name__}")
except KeyError as e:
    print("없는 정보입니다.")


print("=== 사건 2 ===")
try:
    result = "5" + 3
#except Exception as e:
#    print(f"에러내용 : {e}")
#    print(f"에러명칭 : {type(e).__name__}")
except TypeError as e:
    print("문자와 숫자는 연산을 할수 없습니다")



print("=== 사건 3 ===")
try:
    with open("없는파일.txt", "r", encoding="utf-8") as f:
        content = f.read()
#except Exception as e:
#    print(f"에러내용 : {e}")
#    print(f"에러명칭 : {type(e).__name__}")
except FileNotFoundError as e:
    print("존재하지 않은 파일입니다.")