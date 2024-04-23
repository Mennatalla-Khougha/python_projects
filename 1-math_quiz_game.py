"""A simple math playing game"""

print("Welcome to my Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play 😃")
score = 0

answer = input("What's 2(5 + 2)? ")

if answer == "14":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What's (5 + 7) / 3? ")

if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What's 3 * 2 + 7? ")

if answer == "13":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What's 10 / 5  * 3? ")

if answer == "6":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What's 3(3 * 3 + 1)? ")

if answer == "30":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"Your score is ${score} out of 5")