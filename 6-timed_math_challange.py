"""A simple timed math challenge"""
import random 
import time

OPERATORS = ['+', '-', '*',"/"]
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL_PROBLEM = 10

print("Answer to the closest integer")
play = input("Do you want to play? (yes/no) ")

if play.lower() != "yes":
    print("Bye!")
    exit()

print("Let's go!")
print("-------------------------")

start_time = time.time()

def generate_problem():
    """
    The function generates a problem based on the `OPERATORS` and `MIN_OPERAND` and `MAX_OPERAND` variables.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    problem = str(left) + " " + operator + " " + str(right)
    answer = eval(problem)

    return (problem, answer)

wrong_answers = 0

for idx in range(TOTAL_PROBLEM):
    problem, answer = generate_problem()
    while True:
        guess = input(f"Problem # {idx + 1} : {problem} = ")
        if guess == str(int(answer)):
            break
        wrong_answers += 1
end_time = time.time() - start_time

print("-----------------------------")
print("Nice job!")
print(f"You got {TOTAL_PROBLEM - wrong_answers} correct from possible {TOTAL_PROBLEM} problem in {int(end_time)} seconds.")
