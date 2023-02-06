import random

print('Welcome to the Number Guessing Game')
print("I'm thinking of a number of between 1 and 100")
number = int(random.randint(1, 100))
def guess(num):
  result = ''
  if num == number:
    result = 'success'
    return result
  if num > number:
    result = 'Too high\nGuess again'
    return result
  if num < number:
    result = 'Too low\nGuess again'
    return result

def attempt(num):
  num -= 1
  return num

def play():
  choosen = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if choosen == 'easy':
    print("You have 10 attempts remaining to guess the number")
    attempt_num = 10
  elif choosen == 'hard':
    print("You have 5 attempts remaining to guess the number")
    attempt_num = 5
  else:
    print("hard or easy")
  while attempt_num>0:
    guess_num = int(input("Make a guess: "))
    print(guess(guess_num))
    attempt_num = attempt(attempt_num)
    print(attempt_num)
    if guess(guess_num) == 'success':
      break
    if attempt_num == 0:
      print("you use all attempt\nyou lose")

play()
