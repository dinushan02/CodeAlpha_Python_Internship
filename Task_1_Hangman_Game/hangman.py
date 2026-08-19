import random

print("================================")
print("          HANGMAN GAME          ")
print("================================")

print("Welcome to our HANGMAN GAME")

name = input("What is your name: ")
if not name:
    name = "Player"

print(f"Hello {name}, let's play the HANGMAN GAME!")

words = ["red", "blue", "yellow", "black", "green"]

secret_word = random.choice(words)

hidden_word = list("_" * len(secret_word))
print(f"\nWord: {' '.join(hidden_word)}")

my_string = "".join(hidden_word)
incorrect_guesses = 0

guessed_letters = []

while my_string != secret_word and incorrect_guesses < 6:
    user_guess = input("\nEnter a letter: ").lower()

    if user_guess.isalpha() and len(user_guess) == 1:
        if user_guess in guessed_letters:
            print("Already guessed!")
        else:
            guessed_letters.append(user_guess)
            if user_guess in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == user_guess:
                        hidden_word[i] = secret_word[i]
                my_string = "".join(hidden_word)
            else:
                incorrect_guesses += 1
            print(f"\nWord: {' '.join(hidden_word)}")
            print(f"Guessed letters: {', '.join(guessed_letters)}")
            print(f"Incorrect guesses: {incorrect_guesses}/6")
    else:
        print("Please only enter one letter!")

if my_string == secret_word:
    print("\n🎉 Congratulations!")
    print(f"You guessed the word: {secret_word}")
else:
    print("\n💀 Game Over!")
    print(f"The word was: {secret_word}")