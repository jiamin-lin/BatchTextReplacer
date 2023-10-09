import tkinter as tk
from tkinter import filedialog
import os

def set_app_icon(root):
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_path, 'logo.ico')
        root.iconbitmap(icon_path)
    except Exception as e:
        print(e)

def replace_in_files(folder_path, old_cdn_url, new_cdn_url, text_widget, file_extension):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace(old_cdn_url, new_cdn_url)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                text_widget.insert(tk.END, f"已修改文件: {filepath}\n")
                text_widget.see(tk.END)

def on_replace_button_clicked(folder_entry, old_cdn_entry, new_cdn_entry, text_widget, extension_entry):
    folder_path = folder_entry.get()
    old_cdn_url = old_cdn_entry.get()
    new_cdn_url = new_cdn_entry.get()
    file_extension = extension_entry.get()
    replace_in_files(folder_path, old_cdn_url, new_cdn_url, text_widget, file_extension)

def select_directory(folder_entry):
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def main():
    root = tk.Tk()
    root.title("批量文本替换工具")
    

    # Layout frames
    top_frame = tk.Frame(root, padx=20, pady=10)
    top_frame.pack(pady=20)

    middle_frame = tk.Frame(root, padx=20, pady=10)
    middle_frame.pack(pady=20)

    bottom_frame = tk.Frame(root, padx=20, pady=10)
    bottom_frame.pack(pady=20)

    # Top Frame - Folder selection
    folder_label = tk.Label(top_frame, text="选择文件夹:")
    folder_label.grid(row=0, column=0, sticky='w', pady=10)

    folder_entry = tk.Entry(top_frame, width=40)
    folder_entry.grid(row=0, column=1, padx=10)

    folder_button = tk.Button(top_frame, text="浏览", command=lambda: select_directory(folder_entry))
    folder_button.grid(row=0, column=2)

    # Middle Frame - CDN URLs and File extension
    old_cdn_label = tk.Label(middle_frame, text="原始的文本内容:")
    old_cdn_label.grid(row=0, column=0, sticky='w', pady=10)
    old_cdn_entry = tk.Entry(middle_frame, width=50)
    old_cdn_entry.grid(row=0, column=1, padx=10, pady=10)

    new_cdn_label = tk.Label(middle_frame, text="要替换的文本内容:")
    new_cdn_label.grid(row=1, column=0, sticky='w')
    new_cdn_entry = tk.Entry(middle_frame, width=50)
    new_cdn_entry.grid(row=1, column=1, padx=10)

    extension_label = tk.Label(middle_frame, text="文件后缀:")
    extension_label.grid(row=2, column=0, sticky='w', pady=10)
    extension_entry = tk.Entry(middle_frame, width=50)
    extension_entry.grid(row=2, column=1, padx=10, pady=10)
    extension_entry.insert(0, ".html")  # default value

    # Bottom Frame - Replace button and output
    replace_button = tk.Button(bottom_frame, text="替换", command=lambda: on_replace_button_clicked(folder_entry, old_cdn_entry, new_cdn_entry, text_widget, extension_entry))
    replace_button.pack(pady=20)

    text_widget = tk.Text(bottom_frame, height=10, width=60)
    text_widget.pack(padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
