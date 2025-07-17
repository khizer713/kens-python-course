import sys
from rpsx2 import rps
from guess_numberx import gn

def arcade(name='PlayerOne'):
    game_count=0

    def play_arcade():
        nonlocal name

        playerchoice =input(f'\n{name}, Please choose a game:\n1 = Rock, Paper, Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade: ')
        
        if playerchoice not in ["1","2","x"]:
            print(f"{name}, please enter 1, 2 or x")
            return play_arcade()

        if playerchoice.lower()=="x":
            print ("\n🎉🎉🎉")
            print("Thank you for playing the Arcade!\n")
            sys.exit(f"Bye {name}! 👋")        
        elif playerchoice=="1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
            return play_arcade()
        elif playerchoice=="2":
            guess_a_number=gn(name)
            guess_a_number()
            return play_arcade()

    return play_arcade

if __name__ == "__main__":

    import argparse

    parser=argparse.ArgumentParser(
        description="Provides personalized game experience"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True, help="Then name of the person playing the game."
    )

    args=parser.parse_args()

    arcade_choice=arcade(args.name)
    arcade_choice()
