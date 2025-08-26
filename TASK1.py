# Hangman Game

import random

words = ["python", "hangman", "programming", "dynamic", "calculator"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    """
]

print(" Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print(stages[attempts])
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print(" Correct!")
    else:
        attempts -= 1
        print(" Wrong guess!")

if "_" not in guessed:
    print(" You won! The word was:", word)
else:
    print(stages[0])
    print(" You lost! The word was:", word)     
