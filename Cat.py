import random
import math

class Cat:
    def __init__(self,n,g,c,b,a):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a
        self.xpos = 0
        self.ypos = 0
        self.energy = 100
    def Jump(self,height):
        global treat
        #check energy!!
        if self.energy > 5:
            self.Talk()
            #change the ypos
            self.ypos = self.ypos + height
            #make older!
            self.Age()
            #print the ypos
            print(self.ypos)
            #check where the treat is
            if self.xpos == treat.xpos and self.ypos == treat.ypos:
                print("chuuru chuuru chuuru!")
                self.Feed()
                treat = Treat("chuuru")
            #we didin't get the treat
            else:
                print(self.DistanceToTreat(treat))
            #change the ypos back
            self.ypos = self.ypos - height
            #print the ypos again
            print(self.ypos)
        else:
            print("I'm hungry")
    #move function
    def Move(self, distance):
        #check energy!!
        self.xpos = self.xpos + distance
        global treat
        pripnpppt(self.DistanceToTreat(treat))
        #make older!
        self.Age()
        print(self.xpos)
    def Age(self):
        self.age = self.age + 0.1
        #lose energy!!
        self.energy = self.energy - 5
    def Talk(self):
        print("Meow")
    #Get Cat age
    def GetCatAge(self):
        cat_age = self.age * 7
        return cat_age
    #Feed
    def Feed(self):
        self.energy = self.energy + 50
    def DistanceToTreat(self, t):
        #find x and y
        dx = self.xpos - t.xpos
        dy = self.ypos - t.ypos
        #square
        dx = dx * dx
        dy = dy * dy

        #find the distance
        distance = math.sqrt(dx + dy)
        return distance
        



#create a cat
cat = Cat("Tama", "F", "White","Mike", 0)

#age = cat.GetCatAge()
#print(age)
#print(cat.Move(10))

#make a treat
# give it a random position
class Treat:
    def __init__(self,n):
        self.name = n
        self.xpos = random.randint(1,10)
        self.ypos = 0

#make a treat!!!
treat = Treat("chuuru")
#print(treat.xpos)
#print(treat.ypos)
        

#use while loop to check commands
command = input("\n")
while command != "q":

#give commands to cat using functions
    

#if command is j, then jump
    if command == "j":
        cat.Jump(10)

#if command is m, then move
    if command == "m":
        d = int(input("How far?\n"))
        cat.Move(d)
#feed the cat
    if command == "f":
        cat.Feed()
    command = input("\n")
















#self.ypos = ypos + height
#print(self.ypos)
#self.ypos = ypos - height
#print(self.ypos)

class CatTwo:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.color = ""
        self.breed = ""
        self.age = 0

class CatThree:
    def __init__(self,n = "",g = "" ,c = "",b = "",a = 0):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a



cat2 = CatTwo()
cat2.name = "Tama"
cat2.gender = "F"
cat2.color = "White"
cat2.breed = "Mike"

cat3 = CatThree("Tama")
#print(cat3.name)



class Dog:
    def __init__(self,n,g,c,b,a):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a
