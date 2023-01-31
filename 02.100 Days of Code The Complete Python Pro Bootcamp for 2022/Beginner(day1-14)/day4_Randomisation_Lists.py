import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_decimal = random.random() * 5
# print(random_decimal)

# from os import stat
# from turtle import st


# states_of_america = ["Delaware", "Pennsylvania"]
# print(states_of_america[0])
# print(states_of_america[-1])
# states_of_america.append("Hawaii")

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# row = int(position[1]) - 1
# column = int(position[0]) - 1
# map[row][column] = 'X'

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#day4 project
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

image = [rock, paper, scissors]

choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

if choice <= 2 and choice >= 0:
    print(image[choice])
    cp_choice = random.randint(0, 2)
    print(f"Computer chose: {cp_choice}")
    print(image[cp_choice])

    result = choice - cp_choice     
    if result == 1 or result == -2:
        print("You win")
    elif result == 0:
        print("Draw")
    elif result ==-1 or result == 2:
        print("You lose")
else:
    print("You typed invalid number. You lose.")