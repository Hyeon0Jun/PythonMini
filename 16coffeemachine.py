MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
    "money": 0.0,
}


def resources_sufficient(asking):
    if asking=="espresso" or asking=="cappuccino" or asking=="latte":
        resource = ""
        if resources["water"]<MENU[asking]["ingredients"]["water"]:
            resource += "lack of water "
            if resources["milk"]<MENU[asking]["ingredients"]["milk"]:
                resource += "lack of milk "
                if resources["coffee"]<MENU[asking]["ingredients"]["coffee"]:
                    resource += "lack of coffee "
    else:
        return "select menu"
    return resource


def coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(total, asking):
    cost = MENU[asking]["cost"]
    print(total, cost)
    if total>=cost:
        print(f"Here is ${total-cost} in change.")
        print(f"Here is your {asking}. Enjoy!")
        resources["water"] -= MENU[asking]["ingredients"]["water"]
        resources["milk"] -= MENU[asking]["ingredients"]["milk"]
        resources["coffee"] -= MENU[asking]["ingredients"]["coffee"]
        resources["money"] += MENU[asking]["cost"]
    else:
        print("lack of money")


def coffee_machine():
    start_machine = True
    while start_machine:
        asking = input("What would you like? (espresso, latte, cappuccino): ")
        if asking == "report":
            print("water", resources["water"])
            print("milk", resources["milk"])
            print("coffee", resources["coffee"])
            print("money", resources["money"])
        elif asking == "off":
            start_machine = False
        elif resources_sufficient(asking) == "":
            total = coins()
            make_coffee(total, asking)
        else:
            print(resources_sufficient(asking))


coffee_machine()
