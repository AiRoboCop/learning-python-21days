import sys
print("실행 중인 Python: ", sys.executable)

topics = ["변수","조건문","반복문","디버그"]

total = 0

for topic in topics:
    print(topic)
    total += 1

print(f"총 {total}개 배움")