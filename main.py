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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True


def process_coins():
    q = int(input("how many quarters do you have?"))
    d = int(input("how many dimes do you have?"))
    n = int(input("how many nickels do you have?"))
    p = int(input("how many pennies do you have?"))
    total = q * 0.25
    total += d * 0.1
    total += n * 0.05
    total += p * 0.01
    return total


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there are not enough {item}")
            return False
    return True


def payment_accepted(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your {change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("You are too broke to get coffee")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


while machine_on:
    c = input("what would you like?(espresso/latte/cappuccino)")
    if c == "off":
        machine_on = False
    elif c == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[c]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment_accepted(payment, drink["cost"]):
                make_coffee(drink, drink["ingredients"])






