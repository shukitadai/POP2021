import tkinter as tk

root = tk.Tk()

root.title("Listbox")
root.geometry("512x512")

#dca = tk.StringVar()
#dca.set("Camila_cabello Nicholas_galitzine ")

#lb = tk.Listbox(root, listvariable = dca)
#lb.pack()

#cb = tk.Checkbuttton(root)
#cb.pack()

btnText = tk.StringVar()
btn.Text.set("Hello")

x = 1
def change():
    global x
    btnText.set("Hello" + str(x))
    x +=1
    
button = tk.Button(root,textvariable = btnText, command = change)
|abe| = tk.Label(root,textvariable = btnText)
button.pack()
|abe|.pack()


root = mainloop()
