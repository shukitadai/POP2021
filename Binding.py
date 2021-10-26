import tkinter as tk

root = tk.Tk()
root.geometry("512x512")
root.title("Binding")

def apress(event):
    print("a")

def adown(event):
    print("down a")

def aup(event):
    print("up a")    
    
root.bind("<Key-a>",apress)

root.bind("<KeyPress-a>",adown)

root.bind("<KeyRelease-a>",aup)


im = tk.PhotoImage(file = "person.png")

label = tk.Label(root,image = im)

label.place(x=100,y=100,height = 600,\
            width = 500)
