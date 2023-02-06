rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user = int(input())
computer = random.randint(0,2)
rps = [rock,paper,scissors]

if user == 0:
  print('your choose')
  print(rps[user])
  print('computer choose')
  print(rps[computer])
  if computer == 0:
    print('draw')
  elif computer == 1:
    print('lose')
  else:
    print('win')
elif user == 1:
  print('your choose')
  print(rps[user])
  print('computer choose')
  print(rps[computer])
  if computer == 1:
    print('draw')
  elif computer == 2:
    print('lose')
  else:
    print('win')
elif user == 2:
  print('your choose')
  print(rps[user])
  print('computer choose')
  print(rps[computer])
  if computer == 2:
    print('draw')
  elif computer == 0:
    print('lose')
  else:
    print('win')
else:
  print('0or1or2')

