import random
import ascii_arts
import words

logo = ascii_arts.logo
word = random.choice(words.word_list)
stages = ascii_arts.stages

word_len = len(word)
display = []

for _ in range(word_len):
    display += "_"

print(display)

lifes = 6
print(word)
while "_" in display and lifes > 0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")

    for i in range(word_len):
        if word[i] == guess:
            display[i] = guess
    print(display)

    print((" ".join(display)).upper())

    if guess not in word:
        lifes -= 1
        print(f"You guessed {guess} that's not in the word. You lose a life")

    if lifes > 0 and "_" not in display:
        print("You win")

    elif lifes <= 0:
        print("You lose")

    print(stages[lifes])
