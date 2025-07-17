import sys
import random
from enum import Enum

def rps():
    game_count=0
    player_wins=0
    python_wins=0
    tie_games=0

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins
        nonlocal tie_games

        class rps(Enum):
            ROCK=1
            PAPER=2
            SCISSORS=3
        
        playerchoice =input("\nEnter...\n1 for Rock\n2 for Paper, or\n3 for Scissors\n\nEnter Choice Here: ")
        
        if playerchoice not in ["1","2","3"]:
            print("You must enter 1, 2 or 3")
            return play_rps()

        player = int(playerchoice)

        computerchoice=random.choice("123")

        computer=int(computerchoice)

        # print("\nYou Chose "+str(rps(player)).replace("rps.",""))
        # print("Python Chose "+str(rps(computer)).replace("rps.",""))

        print(f"\nYou Chose {str(rps(player)).replace('rps.','').title()}.")
        print(f"Python Chose {str(rps(computer)).replace('rps.','').title()}.\n")
        

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal tie_games

            if player==1 and computer == 3:
                player_wins+=1
                return "🎉 You Win"
            elif player==2 and computer == 1:
                player_wins+=1
                return "🎉 You Win"
            elif player==3 and computer == 2:
                player_wins+=1
                return "🎉 You Win"
            elif player==computer:
                tie_games+=1
                return "😲 Tie Game"
            else:
                python_wins+=1
                return "🐍 Python Wins"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count+=1

        print(f"\nGame Count: {str(game_count)}")
        print(f"Player Wins: {str(player_wins)}")
        print(f"Python Wins: {str(python_wins)}")
        print(f"Tie Games: {str(tie_games)}")
        
        print("\nPlay Again?")

        while True:
            playagain = input("\nPlay Again? \nY for Yes or \nQ for Quit \n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower()=="y":
            return play_rps()
        else:
            print ("\n🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_rps

play=rps()

play()