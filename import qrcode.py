import tkinter as tk

root = tk.Tk()
root.title("smart calculator")
root.geometry("400x600")

enter = tk.Entry(root, font="arial 20")
enter.pack(fill=tk.BOTH, ipadx=8, pady=10)


def click(event):
    current = enter.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            enter.delete(0, tk.END)
            enter.insert(tk.END, str(result))
        except:
            enter.delete(0, tk.END)
            enter.insert(tk.END, "error")
    elif button_text == "c":
        enter.delete(0, tk.END)
    else:
        enter.insert(tk.END, button_text)


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['c']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
