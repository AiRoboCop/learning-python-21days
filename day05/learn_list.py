topics = ["반복문","변수","조건문","함수"]

print(f"배운주재 {topics}")
print(f"주제갯수 {len(topics)}")

print()

print(f"첫번째 {topics[0]}")
print(f"마지막 {topics[-1]}")

print()

topics.append("자료구조")
print(f"추가후 {topics}")
print(f"추가후 갯수 {len(topics)}")

print()

topics[0] = "변수와 입출력"
print(f"주정후 {topics}")

print()
print("지금까지 배운 주제")

for cnt in topics:
    print(cnt)