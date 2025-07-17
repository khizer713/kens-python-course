import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count=0
    player_wins=0
    python_wins=0
    tie_games=0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal tie_games

        class rps(Enum):
            ROCK=1
            PAPER=2
            SCISSORS=3
        
        playerchoice =input(f"\n{name}, enter...\n1 for Rock\n2 for Paper, or\n3 for Scissors\n\nEnter Choice Here: ")
        
        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2 or 3")
            return play_rps()

        player = int(playerchoice)

        computerchoice=random.choice("123")

        computer=int(computerchoice)

        # print("\nYou Chose "+str(rps(player)).replace("rps.",""))
        # print("Python Chose "+str(rps(computer)).replace("rps.",""))

        print(f"\n{name}, chose {str(rps(player)).replace('rps.','').title()}.")
        print(f"Python chose {str(rps(computer)).replace('rps.','').title()}.\n")
        

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            nonlocal tie_games

            if player==1 and computer == 3:
                player_wins+=1
                return f"🎉 {name}, you Win"
            elif player==2 and computer == 1:
                player_wins+=1
                return f"🎉 {name}, you Win"
            elif player==3 and computer == 2:
                player_wins+=1
                return f"🎉 {name}, you Win"
            elif player==computer:
                tie_games+=1
                return f"😲 Tie Game"
            else:
                python_wins+=1
                return f"🐍 Python Wins!\nSorry, {name}.. 🥲"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count+=1

        print(f"\nGame Count: {game_count}")
        print(f"{name}'s Wins: {player_wins}")
        print(f"Python Wins: {python_wins}")
        print(f"Tie Games: {tie_games}")
       
        print(f"\nPlay Again, {name}?")

        while True:
            playagain = input("Y for Yes or \nQ for Quit \n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower()=="y":
            return play_rps()
        else:
            print ("\n🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps

if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser(
        description="Provides a personalized game experience."

    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True, help="Then name of the person playing the game."
    )

    args=parser.parse_args()

    rock_paper_scissors=rps(args.name)
    rock_paper_scissors()