# Global Scope
# enemies = 1

# def increase_enemies():
#     # global enemies
#     # enemies += 1
#     # print(f'enemies inside function: {enemies}')
    
#     print(f'enemies inside function: {enemies}')
#     return enemies + 1    

# enemies = increase_enemies()
# print(f'enemies inside function: {enemies}')


# Global Constraints

# pi = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@shiori_f"


# day13 project

import random

isContinue = True
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def guess_check(answer):
    guess = int(input("Make a guess: "))
    if guess > answer:
        print("Too high.\nGuess again.")
        return False
    elif guess == answer:
        print(f"You got it! The answer was {answer}")
        return True
    else:
        print("Too low.\nGuess again.")
        return False

def setLevel():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

while isContinue:
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")

    attempt = setLevel()
    print(f"You have {attempt} attempts remaining to guess the number.")

    answer = random.randint(1, 100)
    isCorrect = False

    while not isCorrect and attempt > 0:
        isCorrect = guess_check(answer)
        attempt -= 1

    if not isCorrect and attempt == 0:
        print("You couldn't guess the answer.")
    
    next = input("Do you want to try again? Type 'yes' or 'no': ")
    if next == 'yes':
        isContinue = True
    elif next == 'no':
        isContinue = False