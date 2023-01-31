#dictionary

# dictionary = {
#     "A": "aaa",
#     "B": "bbb",
#     "C": "ccc"
# }

# print(dictionary)
# print(dictionary["A"])

# dictionary["D"] = "ddd"

# print(dictionary)

# dictionary["A"] = "AAA"

# print(dictionary)

# for key in dictionary:
#     print(key)
#     print(dictionary[key])

#Nesting

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille"],
#         "total_visits": 12
#     },
#     "Italy": {
#         "cities_visited": ["Roma", "Venezia"],
#         "total_visits": 5
#     }
# }

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille"],
#         "total_visits": 12
#     },
#     {
#         "country": "Italy",
#         "cities_visited": ["Roma", "Venezia"],
#         "total_visits": 5
#     }
# ]

# day9 project

# from replit import clear
import os
from art import logo

print(logo)
dict = {}
next = 'yes'
isNext = True

def find_highest(dict):
    max_bid = 0
    for key in dict:
        if dict[key] > max_bid:
            max_key = key
            max_bid = dict[key]

    print(f"The winner is {max_key} with a bid of ${max_bid}")

while isNext:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dict[name] = bid
    next = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if next == 'yes':
        os.system('cls')
    else:
        isNext = False
        find_highest(dict)
