"""Hangman - a command-line word guessing game.

The player picks a starting letter (A-Z), then guesses letters to
reveal a hidden word. Eight wrong guesses ends the game.
"""

import random
import string

from words import words_per_letter


def choose_category():
    """Ask the player to pick a starting letter and return its word list.

    Loops until a valid A-Z letter with words in it is entered.
    """
    while True:
        choice = input("Pick a starting letter (A-Z): ").strip().upper()

        if len(choice) != 1 or choice not in string.ascii_uppercase:
            print("Please enter a single letter from A to Z.")
            continue

        group = words_per_letter.get(choice, [])

        if not group:
            print(f"No words start with '{choice}'. Try another letter.")
            continue

        return group


def get_valid_word(word_list):
    """Return a random uppercase word with no spaces or hyphens."""
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(word_list)
    return word.upper()


def display_state(lives, used_letters, word):
    """Print the current lives, used letters, and hidden word."""
    print(f"\nYou have {lives} lives left.")
    print("Used letters: " + " ".join(sorted(used_letters)))
    hidden = [letter if letter in used_letters else "-" for letter in word]
    print("Current word: " + " ".join(hidden))


def get_guess(used_letters):
    """Prompt for a single letter, handling empty and invalid input."""
    while True:
        try:
            guess = input("Guess a letter: ").strip().upper()
        except EOFError:
            print("\nInput closed. Exiting.")
            raise SystemExit

        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("Please enter a single letter from A to Z.")
            continue

        if guess in used_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        return guess


def hangman():
    """Run a single game of Hangman from start to finish."""
    print("Welcome to Hangman!")
    word_list = choose_category()
    word = get_valid_word(word_list)

    word_letters = set(word)
    used_letters = set()
    lives = 8

    while word_letters and lives > 0:
        display_state(lives, used_letters, word)
        guess = get_guess(used_letters)
        used_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if lives == 0:
        print(f"\nYou have died. Game over! The word was '{word}'.")
    else:
        print(f"\nYou guessed the word '{word}'! You win!")


if __name__ == "__main__":
    hangman()
