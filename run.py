# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)    #get random word from list
    while "-" in word or " " in word:
        word = random.choice(words)

        return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # adding user input 
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('Try again. You have already guessed that character')

    else:
        print('Try again. You have guessed an invalid character.')

# Call the hangman function to start the game
hangman()