import tkinter as tk

root = tk.Tk()

root.geometry("290x203")

def show_message():
    hello.pack()

hello = tk.Label(root,text = "Hello, world!",cursor = "heart")
#hello.pack()

button = tk.Button(root,text = "Close the window", command = show_message)

entry = tk.Entry(root, text = "Type", show = "*")

entry.pack()
button.pack()
#hello.pack()


root.mainloop()
