import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")

chosen_word_len = len(chosen_word)
display = []

for _ in range(chosen_word_len):
    display += "_"

print(display)

lifes = 6

while "_" in display and lifes > 0:
    guess = input("Guess a letter: ").lower()
    for i in range(chosen_word_len):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lifes -= 1
    print(display)
    print(stages[lifes])

if lifes > 0:
    print("You win")
elif lifes <= 0:
    print("You lose")
