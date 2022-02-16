import tkinter as tk
main_window = tk.Tk()
main_window.geometry("500x200")

tk.Label(main_window, text='INPUT NAME : ').grid(row=0, column=0)
tk.Label(main_window, text='INPUT AGE : ').grid(row=1, column=0)
input_name = tk.Entry(main_window, width=50, borderwidth=5)
input_name.grid(row=0, column=1)
input_age = tk.Entry(main_window, width=50, borderwidth=5)
input_age.grid(row=1, column=1)

def on_click():
    print(f"NAME : {input_name.get()}")
    print(f"AGE : {input_age.get()}")


tk.Button(main_window, text='DONE', command=on_click).grid(row=2, column=1)

main_window.mainloop()

