MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

isRunning = True

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    if "money" in resources:
        print(f"Money: ${resources['money']}")

def check_resource(menu_name):
    ingredients = MENU[menu_name]['ingredients']
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def transaction(menu_name, money):
    order_cost = MENU[menu_name]['cost']
    change = round(money - order_cost, 2)
    if change >= 0:
        if "money" in resources:
            resources["money"] += order_cost
        else:
            resources["money"] = order_cost
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(menu_name):
    order_ingredients = MENU[menu_name]["ingredients"]
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

while isRunning:
    order = input('What would you like? (espresso/latte/cappuccino):')
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        if check_resource(order):
            print('Please insert coins')
            total = int(input('How many quarters?: ')) * 0.25
            total += int(input('How many dimes?: ')) * 0.10
            total += int(input('How many nickles?: ')) * 0.05
            total += int(input('How many pennies?: ')) * 0.01
            if transaction(order, total):
                make_coffee(order)
                print(f"Here is your {order}. Enjoy!")
    elif order == 'report':
        report()
    elif order == 'off':
        isRunning = False
        print('Coffee machine is turned off')
    else:
        print('Please type the correct name in the menu')