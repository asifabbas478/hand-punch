import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

label = tk.Label(root, text="Hello, World!")
label.pack(pady=20)

root.mainloop()
