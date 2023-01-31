# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ?"))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be OK. Have a free to ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
    
#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry, you have to grow taller before you can ride.")

#day3 project
print("Welcome to the treasure island. Your mission is to find the treasure.")
first = input('Do you want to go right or left at the first corner? Please enter "right" or "left".\n').lower()

if first == "left":
    second = input('There is a river in front of you. Do you want to swim or wait for a boat? Please enter "swim" or "wait".\n').lower()
    if second == "wait":
        third = input('There are three doors in front of you. Which door do you choose? Please enter "red", "blue" or "yellow".\n').lower()
        if third == "red":
            print("You are burned by fire. Game Over.")
        elif third == "blue":
            print("You are eaten by beasts. Game Over.")
        elif third == "yellow":
            print("You Win!")
        else:
            print("You made mischoise. Game Over.")
    else:
        print("Oh no! You are attacked by trout. Game Over.")
else:
    print("Oh no! You fell into a hole. Game Over.")