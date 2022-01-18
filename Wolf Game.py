import math
import random

class Position:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def Distance(self, pos):
        dx = self.x - pos.x
        dy = self.y - pos.y

        dx = dx * dx
        dy = dy * dy

        dist = math.sqrt(dx + dy)
        return dist

position1 = Position(0,0)
position2 = Position(5,5)

print(position1.Distance(position2))
        
col = 10
row = col

Map = []
for y in range(row):
    r = []
    for x in range(col):
        #pos = Position(x,0)
        r.append("*")
    Map.append(r)

#Map[0][0] = "W"

def print_map(m):
    for r in reversed(Map):
        s = ""
        for p in r:
            s += p
        print(s)
                               

class Wolf:
    def __init__(self,pos,gen, en = 100, ag = 3):
        self.name = "Ame"
        self.position = pos
        self.age = ag
        self.gender = gen
        self.energy = en
        Map[pos.y][pos.x] = "W"
        
    def Move(self, pos):
        if self.position.y + pos.y >len(Map) or \
        self.position.y +pos.y < 0:
            return
        
        if self.position.x + pos.x >= \
        len(Map[self.position.y + pos.y]) or \
        self.position.x + pos.x < 0:
            return

        if self.energy - 3 < 0:
            return
        if self.position.x + pos.x == deer.position.x and \
           self.position.y + pos.y == deer.position.y:
            return
        
        Map[self.position.y][self.position.x] = "*"
        self.position.x += pos.x
        self.position.y += pos.y
        Map[self.position.y][self.position.x] = "W"
        
        self.age += 0.1
        self.energy -= 3

        if self.position.Distance(deer.position) < 2:
            print("close!")
            

class Deer:
     def __init__(self,pos,gen, en = 100, ag = 3):
        self.name = "Bambi"
        self.position = pos
        self.age = ag
        self.gender = gen
        self.energy = en
        Map[pos.y][pos.x] = "D"
        
     def Move(self, pos):
        if self.position.y + position.y >len(Map) or \
        self.position.y +pos.y < 0:
            return
        
        if self.position.x + pos.x >= \
        len(Map[self.position.y + pos.y]) or \
        self.position.x + pos.x < 0:
            return

        if self.energy-3 < 0:
            return

        Map[self.position.y][self.position.x] = "*"
        self.position.x += pos.x
        self.position.y += pos.y
        Map[self.position.y][self.position.x] = "D"
        
        self.age += 0.1
        self.energy -= 3


wolf = Wolf(Position(5,5),"M",100,3)
deer = Deer(Position(random.randint(0,9), \
                     random.randint(0,9)),"M",100,5)
print_map(Map)

command = ""
command = input("\n")
while command != "q":

    
    command = input("\n")

    if command == "W":
        wolf.Move(Position(0,1))

    if command == "A":
        wolf.Move(Position(-1,0))

    if command == "S":
        wolf.Move(Position(0,-1))
        
    if command == "D":
        wolf.Move(Position(1,0))
        
    print_map(Map)
    command = input("\n")



    
    
