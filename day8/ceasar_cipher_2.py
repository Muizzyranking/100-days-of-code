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


def encrypt(plain_text, shift_amount):
    encript_text = ""
    for letter in plain_text:
        for letter_index in range(len(alphabet)):
            if letter == alphabet[letter_index]:
                shift = shift_amount + letter_index
                if shift > 25:
                    shift -= 26
                encript_text += alphabet[shift]
    print(f"The encoded text is {encript_text}")


def decrypt(plain_text, shift_amount):
    decrypt_text = ""
    for letter in plain_text:
        for letter_index in range(len(alphabet)):
            if letter == alphabet[letter_index]:
                shift = letter_index - shift_amount
                if shift < 0:
                    shift += 26
                decrypt_text += alphabet[shift]
    print(f"The decoded text is {decrypt_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid Direction")
