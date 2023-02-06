from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

isRunning = True

while isRunning:
    order = input(f'What would you like? ({menu.get_items()}):')
    if order == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    elif order == 'off':
        isRunning = False
        print('Coffee machine is turned off')
    else:
        drink = menu.find_drink(order)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)