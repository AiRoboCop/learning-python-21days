import tkinter as tk


def login():
    user_id = id_entry.get()
    password = pw_entry.get()

    if user_id == "" or password == "":
        result_label.config(text="아이디와 비밀번호를 입력하세요", fg="red")
    else:
        result_label.config(text=f"환영합니다, {user_id}님!", fg="green")


def cancel():
    id_entry.delete(0, tk.END)
    pw_entry.delete(0, tk.END)
    result_label.config(text="입력을 취소했습니다", fg="gray")


# === 창 만들기 ===
root = tk.Tk()
root.title("로그인")
root.geometry("360x280")

# === 1) 제목 영역(Frame) ===
title_frame = tk.Frame(root)
title_frame.pack(pady=15)

title_label = tk.Label(title_frame, text="로그인", font=("맑은고딕", 18))
title_label.pack()

# === 2) 입력 영역(Frame + grid) ===
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# 아이디(0행)
tk.Label(input_frame, text="아이디").grid(row=0, column=0, padx=5, pady=5, sticky="e")
id_entry = tk.Entry(input_frame)
id_entry.grid(row=0, column=1, padx=5, pady=5)

# 비밀번호(1행)
tk.Label(input_frame, text="비밀번호").grid(row=1, column=0, padx=5, pady=5, sticky="e")
pw_entry = tk.Entry(input_frame, show="*")
pw_entry.grid(row=1, column=1, padx=5, pady=5)

# === 3) 버튼 영역(Frame + pack) ===
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

login_button = tk.Button(button_frame, text="로그인", command=login, width=8)
login_button.pack(side="left", padx=5)

cancel_button = tk.Button(button_frame, text="취소", command=cancel, width=8)
cancel_button.pack(side="left", padx=5)

# === 4) 결과 영역 ===
result_label = tk.Label(root, text="", font=("맑은고딕", 10))
result_label.pack(pady=10)

# 창 유지
root.mainloop()
