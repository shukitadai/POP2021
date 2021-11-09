import tkinter as tk

class Ingredient:
    def __init__(self,a,u,t):
        self.amount = a
        self.unit = u
        self.thing = t

#    def __str__(self):
#        return str (self.amount) + "\t" +self.unit \
#               + "\t" + self.thing

#    def __repr__(self):
#        return str (self.amount) + "\t" +self.unit \
#               + "\t" + self.thing

#flour = Ingredient(1.75,"cup","all-purpose flour")
#print(flour)

class Recipe:
    def __init__(self,i,d):
        self.ingredients = i
        self.directions = d
#    def print_recipe(self):
#        for ingredient in self.ingredients:
#            print(ingredient)
#        for dir in range (len(self .directions)):
#            print(str(dir + 1) + ". " + self.directions[dir])


root = tk.Tk()
root.geometry("700x500")
root.title("Recipe")

x = 2
def add_ingredient():
    global x
    amount = tk.Entry(root)
    unit = tk.Entry(root)
    thing = tk.Entry(root)

    amount.grid(column = 1, row = x)
    unit.grid(column = 2, row = x)
    thing.grid(column = 3, row = x)
    x += 1
    create_ingredient.place_configure(\
        y = create_ingredient.winfo_y() + 150)

amountLabel = tk.Label(root,text = "Amount")
amountLabel.grid(column = 1,row = 1)

unitLabel = tk.Label(root,text = "Unit")
unitLabel.grid(column = 2, row = 1)

thingLabel = tk.Label(root,text ="ingredient")
thingLabel.grid(column = 3, row = 1)

saveButton = tk.Button(root,text = "Save")
saveButton.place(x=700,y=500,anchor = tk.SE)

plus = tk.PhotoImage(file = "plus.png")
create_ingredient = tk.Button(root, image = plus,\
                              command = add_ingredient)

create_ingredient.place(x=350,y=100, anchor = tk.CENTER)
