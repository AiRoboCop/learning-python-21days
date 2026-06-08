# 전역변수 - 인자 처리

count = 0

def increase(count) -> None:
    return count + 1

count = increase(count)
print(count)

# 전역변수 - global

# count = 0

# def increase() -> None:
#     global count
#     count = count + 2
#     print(count)

# increase()
# print(count)

# 전역변수 - 수정

# count = 0

# def increase() -> None:
#    count = count + 1
#    print(count)

#increase()


# 전역변수 - 읽기

message = "전역 메시지"

def show() -> None:
    print(message)

show()    
print(message)

# 지역변수

def my_func() -> None:
    x = 10
    print(x)

my_func()
#print(x)
    