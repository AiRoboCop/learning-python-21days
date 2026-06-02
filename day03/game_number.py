import random

ran_num = random.randint(1,100)

cnt_loop = 0

while True:

    user_num = int(input("1~100 사이의 숫자를 입력하세요:"))

    cnt_loop += 1

    if user_num < ran_num:
        print("더 큰 수예요!")
    elif user_num > ran_num:
        print("더 작은 수예요!")
#   elif user_num == ran_num:
    else:
        print(f"정답! {cnt_loop}번 만에!")
        break

print("게임 종료")