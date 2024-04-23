"""This a number guessing game"""
import random

top_number_input = input("Type the top number, must be greater than 5: ")

if top_number_input.isdigit():
    top_number = int(top_number_input)

    if top_number <= 5:
        print('The number must be greater than 5')
        quit()
else:
    print("Please Enter a number next time.")
    quit()

random_number = random.randint(0, top_number)
score = 0


while True:
    score += 1
    guess_input = input(f'Guess a number between 0 and {top_number}: ')
    if guess_input.isdigit():
        guess = int(guess_input)
    else:
        print("Please Enter a number next time.")
        continue

    if guess < random_number:
        print('Guess higher')

    elif guess > random_number:
        print('Guess lower')

    else:
        print(f'You won! And it only took you {score} tries')
        break

