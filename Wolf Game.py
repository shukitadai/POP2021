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
        self.enegy = en
        Map[pos.y][pos.x] = "W"
    def Move(self, pos):
        if self.position.y + position.y >len(Map) or //
        self.position.y +pos.y < 0:
            return
        if self.position.x + position.x >= //
        len(Map[self.position.y + pos.y]) or
        self.position.x + position.x < 0:
            return
        


wolf = Wolf(Position(5,5),"M",100,3)
#print_map(Map)

command = ""
command = input("\n")
while command != "q":

    
    command = input("\n")

    if command == "W":

    if command == "A":

    if command == "S":

    if commamd == "D":
        
    command = input("\n")






    
    
