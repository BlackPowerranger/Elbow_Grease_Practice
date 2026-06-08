import sys
import os
import subprocess
from random import randint

if "launched_new_window" not in sys.argv:
    script_path = os.path.abspath(__file__)
    # Use 'start' to open a new separate command window.
    # /c closes the window after the script ends.
    subprocess.run(f'start cmd /c python "{script_path}" launched_new_window', shell=True)
    sys.exit()

round_count=0
player_score_count=0
computer_score_count=0

# Loop for restarting the game
while round_count < 3:
    os.system('cls') # Clear the screen (Windows)

    print("ROUND ", round_count+1)
    player = input("rock(r), paper(p), scissors(s), or quit(q)? ").lower()

    print("You chose:", player)

    if player == "q":
        print("Thanks for playing!")
        break

    if player not in ["r", "p", "s", "q"]:
        print("Invalid input... Please try again.")
        input("Press enter to continue...")
        continue

    chosen = randint(1,3)

    if(chosen == 1):
        computer = "r"
    elif(chosen == 2):
        computer = "p"
    else:
        computer = "s"

    print("Computer chooses: ",computer)

    if (player == computer):
        print("DRAW!")
    elif (
        (player == "r" and computer == "s") or
        (player == "p" and computer == "r") or
        (player == "s" and computer == "p")
    ):
        player_score_count+=1
        print("You win!")
        print("Player score: ", player_score_count , "Computer score: ", computer_score_count )
    else:
        computer_score_count+=1
        print("Computer wins!")
        print("Player score: ", player_score_count , "Computer score: ", computer_score_count )

    input("Press enter to continue...")
    round_count+=1