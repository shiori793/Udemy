from art import logo
from art import vs
from game_data import data
import random
import os

score = 0
isCorrect = True

os.system('cls')
print(logo)

while isCorrect:
    choiceA = random.choice(data)
    choiceB = random.choice(data)
    while choiceA == choiceB:
        choiceB = random.choice(data)
    if choiceA['follower_count'] > choiceB['follower_count']:
        winner = 'a'
    else:
        winner = 'b'

    print(
        f'Compare A: {choiceA["name"]}, {choiceA["description"]}, from {choiceA["country"]}')
    print(vs)
    print(
        f'Against B: {choiceB["name"]}, {choiceB["description"]}, from {choiceB["country"]}')
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system('cls')
    print(logo)

    if answer == winner:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        isCorrect = False
        print(f"Sorry, that's wrong. Final score: {score}")
