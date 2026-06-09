# 파일 쓰기

topics = ["변수","조건문","반복문","함수","자료구조"]

with open("topics.txt", "w", encoding="utf-8") as f:
    for topic in topics:
       f.write(topic + "\n")
#       f.write(topic)

print("파일 저장 완료")
print()

print("파일읽기(한줄만)")

with open("topics.txt", "r", encoding="utf-8") as f:
    print(f.readline().strip())
    print(f.readline().strip())

print("파일읽기(줄의 List)")

with open("topics.txt", "r", encoding="utf-8") as f:
    lists = f.readlines()

    for li in lists:
        print(li.strip())
    

# 파일 읽기(while 활용)
print("파일읽기(while)")

with open("topics.txt", "r", encoding="utf-8") as f:

    while True:
        line = f.readline()

        if line == "":
            break

        print(line.strip())




# 파일 읽기(한번에)
print("파일읽기 (한번에)")
with open("topics.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(f"파일의 내용\n{contents}")

print("파일읽기 (한번에 2)")
with open("topics.txt", "r", encoding="utf-8") as f:
    print(f"파일의 내용\n{f.read()}")    

print("파일읽기 (한번에 3)")
with open("topics.txt", "r", encoding="utf-8") as f:
    print(f"파일의 내용\n{f}")

# 파일 읽기(한줄씩)
print("파일읽기 (한줄씩)")
with open("topics.txt", "r", encoding="utf-8") as f:
    num = 1
    for line in f:
        #print(f"{num} : {line}")
        print(f"{num} : {line.strip()}")
        #print(f"{num} : {line.split()}")
        num += 1

print("파일읽기 (한줄씩) 2")
with open("topics.txt", "r", encoding="utf-8") as f:
    num = 1
#   for line in f.read():
    for line in f:
        print(f"{num} : {line}")
        #print(f"{num} : {line.strip()}")
        #print(f"{num} : {line.split()}")
        num += 1        