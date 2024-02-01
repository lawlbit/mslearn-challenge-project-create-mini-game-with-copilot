# Give me a template for a command line application for a rock-paper-scissors game.
# The game should be able to receive a user's input and randomly generate a choice for the computer.
# The game should then determine the winner and print the result.
# The game should also be able to keep track of the score.
# The game should be able to run until the user decides to quit.
# The game should be able to display the final score when the user decides to quit.

import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'q' to quit the game.")
    user_score = 0
    computer_score = 0
    while True:
        user_input = input("Enter your choice: ")
        if user_input == "q":
            print("Final score:")
            print(f"User: {user_score}")
            print(f"Computer: {computer_score}")
            break
        computer_input = random.choice(["rock", "paper", "scissors"])
        print(f"Computer's choice: {computer_input}")
        if user_input == computer_input:
            print("It's a tie!")
        elif user_input == "rock":
            if computer_input == "scissors":
                print("You win!")
                user_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif user_input == "paper":
            if computer_input == "rock":
                print("You win!")
                user_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif user_input == "scissors":
            if computer_input == "paper":
                print("You win!")
                user_score += 1
            else:
                print("You lose!")
                computer_score += 1
        else:
            print("Invalid input. Please try again.")

main()