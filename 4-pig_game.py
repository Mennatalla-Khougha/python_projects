"""A simple Pig Game"""
import random
from typing import Dict

play = input("Press Enter to play, q to quit: ").lower()

max_score = input("Enter the max score: ")

while max_score.isdigit() != True:
    print("Please enter a valid number")
    max_score = input("Enter the max score: ")

MAX_SCORE = int(max_score)
    

while True:
    players_number = input("Enter a the number of players (2 - 4) : ")

    if players_number.isdigit():
        players = int(players_number)
        if 2 <= players <= 4:
            break    
    else:
        print("Please choose a valid number!")
players_name: Dict[int, str] = {}

for i in range(players):
    players_name[i] = input(f'Enter the name of player {i + 1}: ')

players_score = [0 for _ in range(players)]

def playing(player, score, MAX_SCORE):
    """
    The function simulates a simple dice game where players take turns rolling a dice and accumulating
    points until a maximum score is reached.
    
    @param player The `player` parameter in the `playing` function represents the name of the player who
    is currently taking their turn in the game.
    @param score The `score` parameter in the `playing` function represents the current score of the
    player in the game. It keeps track of the points accumulated by the player as they take turns
    rolling a dice. The player's score is compared to the `MAX_SCORE` to determine the winner of the
    game.
    @param MAX_SCORE MAX_SCORE is the maximum score that a player needs to reach in order to win the
    game. The game continues until a player's score reaches or exceeds this maximum score.
    @return the final score of the player after playing the game.
    """
    while score < MAX_SCORE:
        print(f"{player}'s turn")
        play = input("Press Enter to play, q to quit: ").lower()


        if play == "q":
            print(f"The current score is {score}")
            break
     
        roll = random.randint(1, 6)

        if roll == 1:
            score = 0
            print(f"You rolled {roll} Your current score is {score} and you lose your turn")
            break
        
        else:
            score += roll
            print(f"You rolled {roll} Your current score is {score}")
        
        if score >= MAX_SCORE:
            break
    return(score)

while True:
    for player in range(players):
        players_score[player] = playing(players_name[player], players_score[player], MAX_SCORE)
        if players_score == 0:
            continue

        if players_score[player] >= MAX_SCORE:
            print(f"{players_name[player]} won the game with a score of {players_score[player]}")
            quit()
