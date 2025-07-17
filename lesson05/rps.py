import sys
import random
from enum import Enum

class rps(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

# print(rps(2))
# print(rps.ROCK)
# print(rps['ROCK'])
# print(rps.ROCK.value)
# sys.exit()


print("")

playerchoice =input("Enter...\n1 for Rock\n2 for Paper, or\n3 for Scissors\n\nEnter Choice Here: ")
player = int(playerchoice)

if player <1 or player >3:
    sys.exit("You must enter 1, 2 or 3")

computerchoice=random.choice("123")
computer=int(computerchoice)

print("")
print("You Chose "+str(rps(player)).replace("rps.",""))
print("Python Chose "+str(rps(computer)).replace("rps.",""))
print (" ")

if player==1 and computer == 3:
    print("🎉 You Win")
elif player==2 and computer == 1:
    print("🎉 You Win")
elif player==3 and computer == 2:
    print("🎉 You Win")
elif player==computer:
    print("😲 Tie Game")
else:
    print("🐍 Python Wins")
