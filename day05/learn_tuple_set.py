# 튜플

point = (10, 20)

print(f"자표 : {point}")
print(f"x : {point[0]}, y : {point[1]}")

# 세트
name = ["김철수", "안철수", "김철수", "박민수"]
unique_name = set(name)

print(f"원본 : {name}")
print(f"중복 제거 : {unique_name}")
print(f"실제 인원 : {len(unique_name)}")
print(f"unique_name type : {type(unique_name)}")