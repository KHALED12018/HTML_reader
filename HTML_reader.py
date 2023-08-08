import re
import tkinter as tk
from tkinter import filedialog

def open_html_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*")])
    if file_path:
        with open(file_path, 'r') as file:
            html_content = file.read()
            html_codes = extract_html_codes(html_content)
            extracted_codes = "\n".join(html_codes)
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, extracted_codes)
            result_text.config(state=tk.DISABLED)
            scrollbar.set(0.0, 0.0)
            separator_label.config(text="------------------")

def extract_html_codes(text):
    html_codes = re.findall(r'<[^>]+>', text)
    return html_codes

root = tk.Tk()
root.title("HTML Code Extractor")

open_button = tk.Button(root, text="Open HTML File", command=open_html_file)
open_button.pack()

separator_label = tk.Label(root, text="------------------")
separator_label.pack()

result_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
result_text.pack()

scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
