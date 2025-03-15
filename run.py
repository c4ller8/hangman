# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words

def get_valid_word(words):
    word = random.choice(words):    #get random word from list
    while "-" in word or " " in word:
        word = random.choice(words)

        return word
