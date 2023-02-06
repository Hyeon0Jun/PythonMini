import os
clear = lambda: os.system('cls')
clear()

auction = {}
win = 0
winner = ""
person = "yes"
while person=="yes":
  name = input("What's your name: ")
  clear()
  bill = int(input("What's your bid: "))
  person = input("yes or no: ")
  auction[name] = bill
  clear()
for person in auction:
  if win<auction[person]:
    win=auction[person]
    winner=person
print(winner,win)
clear()