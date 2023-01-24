# print("Hello"[4])
# print("123"+"456")

# print(123 + 456)

# a = 123;
# b = str(a)
# print(type(a))
# print(type(b))

# height = input("what is your height? ")
# print(height);
# height_int = int(height);
# print(round(2.6666666,2))

# score = 0
# height = 1.8
# isWinning = True
# #f-string
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#day2 project
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
#bill = float(input("What was the total bill? $"))
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
#percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = input("How many people to split the bill? ")
#people = int(input("How many people to split the bill? "))

f_bill = float(bill)
i_percentage = int(percentage) / 100
i_people = int(people)

pay = round(f_bill * (1 + i_percentage) / i_people, 2)

print(f"Each person should pay: ${pay}")