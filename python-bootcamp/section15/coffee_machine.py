# Program Requirements
# 1. Print report.
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make Coffee.

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

profit = 0


def is_resource_sufficient(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def cal_coins():
    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))  # 25 cents
    dimes = int(input("how many dimes?: "))  # 10 cents
    nickles = int(input("how many nickles?: "))  # 5 cents
    pennies = int(input("how many pennies?: "))  # 1 cent

    cents_to_dollars = (quarters*25 + dimes*10 + nickles*5 + pennies) / 100
    return cents_to_dollars


def is_coins_sufficient(inserted_coins, coffee_cost):
    if inserted_coins < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(inserted_coins - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += coffee_cost
        return True


def make_coffee(order, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order} ☕️. Enjoy!")


def start_coffee_machine():
    is_on = True

    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == "off":
            is_on = False
        elif order == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            ordered_coffee = MENU[order]
            ordered_coffee_ingredients = ordered_coffee["ingredients"]
            ordered_coffee_cost = ordered_coffee["cost"]
            if is_resource_sufficient(ordered_coffee_ingredients):
                inserted_coins = cal_coins()
                if is_coins_sufficient(inserted_coins, ordered_coffee_cost):
                    make_coffee(order, ordered_coffee_ingredients)


start_coffee_machine()
