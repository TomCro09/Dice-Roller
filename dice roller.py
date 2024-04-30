import random

def roll(d20,d12,d10,d8,d6,d4):
    if player_roll == "d20":
        roll = random.choice(d20)
        return roll
    if player_roll == "d12":
        roll = random.choice(d12)
        return roll
    if player_roll == "d10":
        roll = random.choice(d10)
        return roll
    if player_roll == "d8":
        roll = random.choice(d8)
        return roll
    if player_roll == "d6":
        roll = random.choice(d6)
        return roll
    if player_roll == "d4":
        roll = random.choice(d4)
        return roll
    

d20 = ["20","19","18","17","16","15","14","13","12","11","10","9","8","7","6","5","4","3","2","1"]
d12 = ["12","11","10","9","8","7","6","5","4","3","2","1"]
d10 = ["10","9","8","7","6","5","4","3","2","1"]
d8 = ["8","7","6","5","4","3","2","1"]
d6 = ["6","5","4","3","2","1"]
d4 = ["4","3","2","1"]

print("d20")
print("d12")
print("d10")
print("d8")
print("d6")
print("d4")     

while True:
    player_roll = input("Which dice would you like to roll: ")
    print(roll(d20,d12,d10,d8,d6,d4))
