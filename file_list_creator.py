import tkinter as tk
from tkinter import filedialog, messagebox

def save_file_list():
    file_list = text_box.get("1.0", tk.END).strip()
    if not file_list:
        messagebox.showwarning("警告", "ファイルリストが空です")
        return

    # ファイル名を大文字に変換
    file_list_upper = "\n".join([line.upper() for line in file_list.splitlines()])

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_list_upper)

    messagebox.showinfo("完了", "ファイルリストが保存されました", font=("Arial", 18))  # フォントサイズを大きくする

def update_status():
    line_count = text_box.index(tk.END).split('.')[0]
    status_label.config(text=f"ただいま {line_count} 個目のデータを入力中")

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("ファイルリスト作成ツール")

# ウィンドウのサイズを変更（幅 x 高さ）
root.geometry("500x550")  # ウィンドウのサイズを大きくする（例: 500x550ピクセル）

# ウィンドウの背景色を変更
background_color = '#abcfd1'
root.configure(bg=background_color)

# フレームの作成とパディングの設定
frame = tk.Frame(root, padx=20, pady=20, bg=background_color)
frame.pack(padx=20, pady=20)

# テキストボックスの作成
text_box = tk.Text(frame, width=40, height=15, font=("Arial", 14))
text_box.pack(padx=10, pady=10)

# ステータスラベルの作成
status_label = tk.Label(frame, text="", font=("Arial", 12), bg=background_color)
status_label.pack(pady=10)

# ボタンの作成とパディングの設定
button = tk.Button(frame, text="ファイルリストを保存", command=save_file_list, width=20, height=2, bg='white', fg='black')
button.pack(padx=10, pady=10)

# 初期のカウントを設定
data_count = 0

def count_data(event):
    global data_count
    if event.char and event.char != '\x08':  # 文字が入力された場合（バックスペースを除く）
        data_count += 1
    update_status()

# テキストボックスにバインディングして、データが入力されたときにカウントを更新
text_box.bind("<KeyRelease>", count_data)

# イベントループの開始
root.mainloop()
