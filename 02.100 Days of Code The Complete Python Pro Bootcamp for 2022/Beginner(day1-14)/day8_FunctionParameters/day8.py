# def hello(a, b):
#     print(f"{a}")
#     print(f"{b}")

# hello("a", "b")
# hello(b = "b", a = "a")

#day8 project
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    result = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        index = alphabet.index(letter) + shift
        if index >= len(alphabet):
            index -= len(alphabet)
        result += alphabet[index]
    print(f"The {direction}d text is {result}")

next = True
while next:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if result == "no":
        next = False

# def encrypt(text, shift):
#     result = ""
#     for letter in text:
#         index = alphabet.index(letter) + shift
#         if index >= len(alphabet):
#             index -= len(alphabet)
#         result += alphabet[index]
#     print(f"The encoded text is {result}")

# def decrypt(text, shift):
#     result = ""
#     for letter in text:
#         index = alphabet.index(letter) - shift
#         result += alphabet[index]
#     print(f"The decoded text is {result}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)