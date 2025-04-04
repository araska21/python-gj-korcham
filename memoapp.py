import tkinter as tk
from tkinter import messagebox

def add_memo():
    memo = entry.get()
    if memo:
        with open('memo.txt', 'a', encoding='utf-8') as f:
            f.write(memo + '\n')
        entry.delete(0, tk.END)
        messagebox.showinfo("정보", "메모가 추가되었습니다.")
    else:
        messagebox.showwarning("경고", "메모를 입력해 주세요.")

def view_memos():
    try:
        with open('memo.txt', 'r', encoding='utf-8') as f:
            memos = f.read()
            text_area.delete(1.0, tk.END)  # Clear previous text
            text_area.insert(tk.END, memos)  # Display memos
    except FileNotFoundError:
        messagebox.showwarning("경고", "메모 파일이 존재하지 않습니다.")

# GUI 설정
root = tk.Tk()
root.title("메모 어플리케이션")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="추가", command=add_memo)
add_button.pack(side=tk.LEFT)

view_button = tk.Button(frame, text="보기", command=view_memos)
view_button.pack(side=tk.LEFT)

text_area = tk.Text(root, height=10, width=60)
text_area.pack(pady=10)

root.mainloop()