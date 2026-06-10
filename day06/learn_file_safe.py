def read_file_safe(filename : str) -> None:
    """파일을 안전하게 읽기(없어도 안 죽음)"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{filename} 파일을 찾을 수 없습니다.")
    else:
        print(f"파일 내용 : {content}")
    
    finally:
        print(f"--- '{filename}' 읽기 시도 완료 ---")

with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("오늘 배운 것 : 예외 처리 \n")
    f.write("내일 배울 것 : 클래스(OOP) \n")

print("=== 있는 파일 ===")
read_file_safe("memo.txt")

print()
print("=== 없는 파일 ===")
read_file_safe("없는파일.txt")

