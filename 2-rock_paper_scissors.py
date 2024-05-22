"""This is a simple Rock Paper Scissors game"""
import random

player_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Please type rock, paper or scissors to play or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("please type a valid option")
        continue

    random_number = random.randint(0, 2)
    computer_guess = options[random_number]
    print(f"The computer chose {computer_guess}")

    if user_input == computer_guess:
        print("It's a tie!")
    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        player_wins += 1
    elif user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        player_wins += 1
    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        player_wins += 1
    else:
        print("You lost!")
        computer_wins += 1  

print(f"The user won {player_wins} times and the computer won {computer_wins} times")
