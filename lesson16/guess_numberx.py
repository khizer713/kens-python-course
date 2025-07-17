import sys
import random

def gn(name='PlayerOne'):
    game_count=0
    player_wins=0
    python_wins=0

    print(f"\n{name} Welcome to the Arcade game Guess My Number!\n\n")

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        playerchoice =input(f"\n{name}, please enter 1, 2 or 3 here: ")
        
        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2 or 3")
            return play_gn()

        player = int(playerchoice)

        computerchoice=random.choice("123")

        computer=int(computerchoice)

        print(f"\n{name}, chose {playerchoice}.")
        print(f"Python chose {computerchoice}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player==computer :
                player_wins+=1
                return f"🎉 {name}, you Win"
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
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay Again, {name}?")

        while True:
            playagain = input("Y for Yes or \nQ for Quit \n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower()=="y":
            return play_gn()
        else:
            print ("\n🎉🎉🎉")
            print("Thank you for playing Guess My Number!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return play_gn

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

    guess_a_number=gn(args.name)
    guess_a_number()