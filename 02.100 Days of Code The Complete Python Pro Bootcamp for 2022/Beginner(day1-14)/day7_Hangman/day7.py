import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

# word_list = ["aardvark", "baboon", "camel"]
print(logo)

choice = random.choice(word_list)
# print(f"chosen word is {choice}")
word_length = len(choice)

display = []
for _ in range(word_length):
    display += "_"
# print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = choice[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in choice:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])