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
        if self.position.y + pos.y >len(Map) or \
        self.position.y +pos.y < 0:
            return
        
        if self.position.x + pos.x >= \
        len(Map[self.position.y + pos.y]) or \
        self.position.x + pos.x < 0:
            return

        if self.energy-3 < 0:
            return

        if self.position.x + pos.x == deer.position.x and \
           self.position.y + pos.y == deer.position.y:
            return
            

        Map[self.position.y][self.position.x] = "*"
        self.position.x += pos.x
        self.position.y += pos.y
        Map[self.position.y][self.position.x] = "D"
        
        self.age += 0.1
        self.energy -= 3

     def Notice(self):
        if self.position.Distance(wolf.position) <= 4:
            #print("Danger Danger Danger")
            return True
        else:
            return


wolf = Wolf(Position(5,5),"M",100,3)
deer = Deer(Position(random.randint(0,9), \
                     random.randint(0,9)),"M",100,5)
print_map(Map)

command = ""
command = input("\n")
while command != "q":

    
    command = input("\n")

    if command == "w":
        wolf.Move(Position(0,1))

    if command == "a":
        wolf.Move(Position(-1,0))

    if command == "s":
        wolf.Move(Position(0,-1))
        
    if command == "d":
        wolf.Move(Position(1,0))

    if deer.Notice():
        notice_chance = random.randint(0,9)
        if notice_chance >= 4:
            wolf_to_deer = Position(\
                deer.position.x - wolf.position.x,\
                deer.position.y - wolf.position.y)
            print(wolf_to_deer.x)
            print(wolf_to_deer.y)

            wolf_deer_distance = deer.position.Distance(wolf.position)
            wolf_to_deer.x = wolf_to_deer.x/wolf_deer_distance
            wolf_to_deer.y = wolf_to_deer.y/wolf_deer_distance
            print(wolf_to_deer.x)
            print(wolf_to_deer.y)

            deer.Move(Position(math.floor(wolf_to_deer.x * 3),\
                               math.floor(wolf_to_deer.y *3)))

          
    print_map(Map)
    command = input("\n")



    
    
