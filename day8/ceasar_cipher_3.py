alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(text, shift_amount, direction):
    crypted_text = ""
    shift = 0
    for letters in text:
        for letter_index in range(len(alphabet)):  # alphabet:
            if letters == alphabet[letter_index]:
                if direction == "encode":
                    shift = letter_index + shift_amount
                    while shift > 25:
                        shift -= 26
                elif direction == "decode":
                    shift = letter_index - shift_amount
                    while shift < 0:
                        shift += 26
        crypted_text += alphabet[shift]
    if direction == "encode":
        direction = "Encrypted"
    elif direction == "decode":
        direction = "Decrypted"
    print(f"Your {direction} text is: {crypted_text}")


ceasar(text, shift, direction)
