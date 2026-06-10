import os
import time
from random import randint


def get_hint(number): #Hint whether the number is less than, greater than, or equal to 50
    if number < 50:
        return "The number is less than 50."
    elif number > 50:
        return "The number is greater than 50."
    else:
        return "The number is exactly 50."
    
def gameplay(): # main game mechanics
    start_time = time.time()
    quit_out()
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.")

    number_to_guess = randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
           
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            result = (user_guess > number_to_guess) - (user_guess < number_to_guess)  #determines if guess is high, low, or correct
            messages = {
                -1: f"Too low! Try again. {get_hint(number_to_guess)}",
                 1: f"Too high! Try again. {get_hint(number_to_guess)}",
                 0: f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts."
            }

            print(messages[result])
            guessed_correctly = result == 0
           

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds.")
    loop()       
       
def loop():# loop to restart the game
    choices = {'y': True, 'n': False}
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in choices:
            if choices[play_again]:
                os.system('cls' if os.name == 'nt' else 'clear')
                gameplay()
            else:
                print("Thanks for playing! Goodbye!")
                quit()
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def quit_out():# option to quit at the start of the game
    quit_input = input("Press q to quit or press Enter to continue: ")
    if quit_input.lower() == 'q':
        print("Thanks for playing! Goodbye!")
        quit()

def main():
    gameplay()

if __name__ == "__main__":
    main()