import random
from game_data import data


def compare(person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return 'A'
    if person1['follower_count'] < person2['follower_count']:
        return 'B'


def game():
    win = 0
    new_data = data.copy()
    first = random.choice(new_data)
    while True:
        new_data.remove(first)
        print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
        print('vs')
        second = random.choice(new_data)
        print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}")
        select = input("Who has more followers? Type 'A' or 'B': ")
        print("")
        if select == 'A':
            if compare(first, second) == 'A':
                win += 1
                print(f"correct number {win}")
            else:
                print("you lose")
                break
        elif select == 'B':
            if compare(first, second) == 'B':
                win += 1
                print(f"correct number {win}")
            else:
                print("you lose")
                break
        else:
            print("A or B")
            break
        first = second

game()