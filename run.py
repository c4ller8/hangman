# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string


def get_valid_word(words):
    """function gets valid word from list"""
    # get random word from list
    list_words = ['dog', 'cat', 'cactus', 'alpha']
    word = random.choice(list_words)
    print(word)
    while "-" in word or " " in word:
        word = random.choice(words)

        return word.upper()


def hangman():
    word = get_valid_word(words)
    # letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    # what the user has guessed
    used_letters = set()

    lives = 8

    # adding user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(
            'You have',
            lives,
            'lives left and you have used these letters: ',
            ' '.join(used_letters)
        )

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word
        ]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                # tales away a life if wrong
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('Try again. You have already guessed that character')

        else:
            print('Try again. You have guessed an invalid character.')
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You have died Game Over! THe word was'. word)
    else:
        print('You guessed the word', word, '!!')


# Call the hangman function to start the game
hangman()
