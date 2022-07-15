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
money_in_machine = 0


def grab_coffee(name):
    global resources
    global money_in_machine
    water = MENU[name]["ingredients"]["water"]
    if name != "espresso":
        milk = MENU[name]["ingredients"]["milk"]
    else:
        milk = 0
    coffee = MENU[name]["ingredients"]["coffee"]
    cost = MENU[name]["cost"]
    if water > resources['water']:
        return "Not enough water"
    elif coffee > resources['coffee']:
        return "Not enough coffee"
    elif milk > resources['milk']:
        return "Not enough milk"
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        quarters = quarters * 0.25
        dimes = dimes * 0.1
        nickles = nickles * 0.05
        pennies = pennies * 0.01
        money = quarters + dimes + nickles + pennies
        if money >= cost:
            change = money - cost
            money_in_machine += cost
            resources['water'] -= water
            resources['milk'] -= milk
            resources['coffee'] -= coffee
            return f"Your change is {round(change, 2)}$. Here's your {name}. Enjoy!"
        else:
            return f"Not enough money, you inserted {money}$ and the cost is {cost}$"


on = True
print(f"For other commands type 'manual'.\n")
while on:
    user_input = input("What would you like?(espresso/latte/cappuccino): ")

    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        print(grab_coffee(user_input))
    if user_input == "money":
        print(f"Money in machine: {money_in_machine}")

    if user_input == "manual":
        print(
            "Commands are: off(for turning machine off), money(for checking money in machine, report(for checking "
            "resources in the machine)")

    if user_input == "off":
        on = False

