import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")

chosen_word_len = len(chosen_word)
display = []

for _ in range(chosen_word_len):
    display += "_"

print(display)

# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and
#'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i in range(chosen_word_len):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

print("You win")
