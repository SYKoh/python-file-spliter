import tkinter as tk
from tkinter import filedialog

def split_file(input_file, output_file_prefix, chunk_size):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for i in range(0, len(lines), chunk_size):
        output_file = f"{output_file_prefix} {i + 1}-{i + chunk_size}.txt"
        with open(output_file, 'w') as f:
            f.writelines(lines[i:i + chunk_size])

def select_file():
    file_path = filedialog.askopenfilename(title="选择文件")
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def execute_split():
    input_file = file_entry.get()
    output_prefix = output_prefix_entry.get()
    chunk_size = int(chunk_size_entry.get())
    split_file(input_file, output_prefix, chunk_size)
    result_label.config(text="文件分割完成！")

# 创建主窗口
window = tk.Tk()
window.title("文件分割工具")

# 文件选择部分
file_label = tk.Label(window, text="选择文件:")
file_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

file_entry = tk.Entry(window, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(window, text="浏览", command=select_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# 输出文件前缀
output_prefix_label = tk.Label(window, text="输出文件前缀:")
output_prefix_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

output_prefix_entry = tk.Entry(window, width=50)
output_prefix_entry.grid(row=1, column=1, padx=10, pady=10)

# 分割大小
chunk_size_label = tk.Label(window, text="分割大小:")
chunk_size_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

chunk_size_entry = tk.Entry(window, width=10)
chunk_size_entry.grid(row=2, column=1, padx=10, pady=10)

# 执行按钮
execute_button = tk.Button(window, text="执行", command=execute_split)
execute_button.grid(row=3, column=0, columnspan=3, pady=10)

# 结果标签
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# 启动主循环
window.mainloop()
