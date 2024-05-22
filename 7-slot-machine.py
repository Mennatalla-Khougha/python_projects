"""Slot machine"""

import random

def money() -> int:
    """
    Prompts the user to enter the amount of money they would like to deposit.
    Validates the input and returns the balance as an integer.

    Returns:
        int: The balance amount entered by the user.
    """
    while True:
        deposit = input("How much would you like to deposit? $")

        if deposit.isdigit():
            balance = int(deposit)
            if balance > 0:
                return balance
            else:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")
    return balance


def play(bet, balance) -> int:
    """
    Simulates a slot machine game and returns the updated balance after playing.

    Parameters:
    - bet (int): The amount of money to bet on the slot machine.
    - balance (int): The current balance of the player.

    Returns:
    - int: The updated balance after playing the slot machine.

    The function subtracts the bet amount from the balance and randomly selects three items from a list of choices.
    It then checks if all three items are the same. If they are, the player wins a certain amount based on the item,
    and the winnings are added to the balance. If the items are not the same, the player loses the bet amount.
    The function prints the result of the game and returns the updated balance.
    """

    balance -= bet
    choices = ["apple", "orange", "bar", "seven" "heart", "diamond"]
    slot1 = random.choice(choices)
    slot2 = random.choice(choices)
    slot3 = random.choice(choices)
    
    print("---------------------------")
    print(f"| {slot1} | {slot2} | {slot3} |")
    print("---------------------------")
    
    if slot1 == slot2 == slot3:
        for idx in range(6):
            if slot1 == choices[idx]:
                winnings = bet * ((idx + 1) * 2)
                balance += winnings 
        print(f"Congrats you have won ${winnings} your balance is ${balance}")
    else:
        print(f"Sorry you have lost ${bet} your balance is ${balance}")
    
    return balance

def gambling() -> int:
    """
    Simulates a gambling game where the player can place bets on a slot machine.
    The function returns the final balance after the player decides to cash out.

    Returns:
        int: The final balance after the player decides to cash out.
    """
    balance = money()
    count = 0

    while balance >= 0:
        bet = 0
        if count > 0:
            gamble = input("Press Enter if you want to play, N if you want to cash out (Enter / N): ")
            if gamble.lower() == "n":
                return balance
        else:
            count += 1
        if balance > 0:
            betting = input("Please insert your bet? $ ")
            if betting.isdigit() and int(betting) > 0:
                bet = int(betting)
            else:
                print("Please enter a valid number")
                continue
            if bet <= balance:
                balance = play(bet, balance)
            else:
                print("You do not have enough money to make that bet")
        else:
            if bet > 0:
                print("You do not have enough money to make that bet")
            deposit = input("would you like to make a deposit? (Y/N): ")
            if deposit.lower() == "y":
                balance += money()
            else:   
                continue

    return balance


if __name__ == "__main__":
    print(gambling())
