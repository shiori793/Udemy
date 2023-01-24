# def format_name(f_name, l_name):
    # """function to take a first and last name and format it to return the title case version of the name """
#     if f_name == "" or l_name == "":
#         return "You didn't input your name"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("angela", "ANGELA")
# print(formated_string)

# print(format_name(input("What is your first name?"), input("What is your last name?")))

# def is_leap(year):
#   is_leap_year = False
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#           is_leap_year = True
#         #   print("Leap year.")
#     #   else:
#         # print("Not leap year.")
#     else:
#     #   print("Leap year.")
#         is_leap_year = True
# #   else:
#     # print("Not leap year.")
#   return is_leap_year

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap_year(year):
#     if month == 2:
#       return month_days[month - 1] + 1
#     else:
#       return month_days[month - 1]
#   else:
#     return month_days[month - 1]



# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


#day10 project calculator

# from replit import clear
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(): 
    print(logo)
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = int(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # operation_symbol = input("Pick another operation: ")
        # num3 = int(input("What's the next number?: "))
        # calculation_function = operations[operation_symbol]
        # second_answer = calculation_function(first_answer, num3)

        # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer;
        else:
            should_continue = False
            calculator()

calculator()