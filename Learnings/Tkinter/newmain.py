import tkinter as tk

root = tk.Tk()
root.title("Simple App")
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# root.tk.call('tk', 'scaling', 2.0)
# root.geometry("250x250")
# def onclick():
#     print("Testing")
#     lbl.config(text="After Clicking", background="purple")
#
#
# lbl = tk.Label(root, text="Label 1")
# lbl.grid(row=0, column=0)
#
# key = lbl.config().keys()
# print(key)
#
# btn = tk.Button (root, text="Click", command=onclick)
# btn.grid( row=0, column=1)


def add_to_list(event = None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row= 0, column=0, sticky="nsew")

frame.columnconfigure(0,weight=1)
frame.rowconfigure(1,weight=1)

entry = tk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list)

entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, sticky="nsew", columnspan=2)

root.mainloop()