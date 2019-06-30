"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def play_again():
    play_again = input("Would you like to play again? Y/N ")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Thank you for playing. Goodbye!")

def start_game():
    # Store a random number as the answer/solution.
    ANSWER = random.randint(1,10)
    # Continuously prompt the player for a guess.
    attempts = 1
    try:
        guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
    except ValueError as err:
        print("Uh oh! That's not a valid value. Please try again...".format(err))
    while guess != ANSWER:
        try:
            guess = int(guess)
        except ValueError as err:
            print("Uh oh! That's not a valid value. Please try again...".format(err))
            guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
        else:
            #   If the guess is outside the guessing range, try again.
            if guess > 10:
                print("That number is out of range! Choose a number between 1 and 10...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
            elif guess < 1:
                print("That number is out of range! Choose a number between 1 and 10...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
        #   If the guess greater than the solution, display to the player "It's lower".
            elif guess > ANSWER:
                print("It's lower...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
        #   If the guess is less than the solution, display to the player "It's higher".
            elif guess < ANSWER:
                print("It's higher...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
    #   Once the guess is correct, stop looping, inform the user they "Got it"
    if guess == ANSWER:
        print("You got it, {}!".format(name))
        play_again()
    else:
        play_again()

if __name__ == '__main__':
    # Display an intro/welcome message to the player.
    name = input("Hello! What is your name? ")
    print("Hi, {}! Welcome to the Number Guessing Game!".format(name))
    print("There isn't a high score to beat... yet!")
    # Kick off the program by calling the start_game function.
    start_game()