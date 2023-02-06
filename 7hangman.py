import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
live = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(stages[live])
while display.count('_') != 0:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print(f"you've already guessed {guess}")
            if display[position] == letter:
                live -= 1
                print(stages[live])
            else:
                display[position] = letter

    if guess not in chosen_word:
        live -= 1
        print(stages[live])
    if live == 0:
        print('end_game')
        break

    print(display)
# import random
# from hangman_art import stages, logo
# from hangman_words import word_list
# from replit import clear
#
# print(logo)
# game_is_finished = False
# lives = len(stages) - 1
#
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not game_is_finished:
#     guess = input("Guess a letter: ").lower()
#
#     # Use the clear() function imported from replit to clear the output between guesses.
#     clear()
#
#     if guess in display:
#         print(f"You've already guessed {guess}")
#
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(f"{' '.join(display)}")
#
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             game_is_finished = True
#             print("You lose.")
#
#     if not "_" in display:
#         game_is_finished = True
#         print("You win.")
#
#     print(stages[lives])