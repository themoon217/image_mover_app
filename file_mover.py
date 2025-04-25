import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import chardet  # chardet モジュールのインポート

def move_files():
    source_dir = filedialog.askdirectory(title="移動元のフォルダを選択")
    if not source_dir:
        return
    
    destination_dir = filedialog.askdirectory(title="移動先のフォルダを選択")
    if not destination_dir:
        return

    files_to_move_path = filedialog.askopenfilename(title="ファイルリストを選択", filetypes=[("Text Files", "*.txt")])
    if not files_to_move_path:
        return
    
    # ファイルリストの文字エンコーディングを推測する
    with open(files_to_move_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    # ファイルリストを指定されたエンコーディングで読み込む
    with open(files_to_move_path, 'r', encoding=encoding) as file:
        files_to_move = file.read().splitlines()

    # ファイルリストを大文字に変換
    files_to_move = [file_name.upper() for file_name in files_to_move]

    # 確認ダイアログを表示
    confirm = messagebox.askyesno("確認", "移動を開始してもよろしいですか？")
    if not confirm:
        messagebox.showinfo("キャンセル", "処理を中止しました。")
        return

    for file_number in files_to_move:
        file_name = f'{file_number}.jpg'  # ファイル名のフォーマットに合わせて変更
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            messagebox.showwarning("警告", f'{file_name} が見つかりません')

    messagebox.showinfo("完了", "ファイルの移動が完了しました")

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("画像を移動するアプリ")

# ウィンドウのサイズを変更（幅 x 高さ）
root.geometry("400x250")  # ウィンドウのサイズを大きくする（例: 800x600ピクセル）

# ウィンドウの背景色を変更
background_color = '#abcfd1'
root.configure(bg=background_color)

# フレームの作成とパディングの設定
frame = tk.Frame(root, padx=20, pady=20, bg=background_color)  # フレームのパディングを大きくする
frame.pack(padx=20, pady=20)

# ボタンの作成とパディングの設定
button = tk.Button(frame, text="移動を開始します", command=move_files, width=40, height=4,  bg='white', fg='black')  # ボタンの幅と高さを設定
button.pack(padx=40, pady=40)

# イベントループの開始
root.mainloop()

