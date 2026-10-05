# Manual Testing — Hangman

All tests run locally with `python3 run.py` and on the deployed Heroku app.

| #   | Test                   | Input              | Expected                                    | Actual      | Pass |
| --- | ---------------------- | ------------------ | ------------------------------------------- | ----------- | ---- |
| 1   | Empty input (category) | (Enter)            | "Please enter a single letter from A to Z." | as expected | ✅   |
| 2   | Number (category)      | `5`                | Same message                                | as expected | ✅   |
| 3   | Two letters (category) | `ab`               | Same message                                | as expected | ✅   |
| 4   | Valid category         | `C`                | Proceeds with C-words                       | as expected | ✅   |
| 5   | Empty input (guess)    | (Enter)            | "Please enter a single letter from A to Z." | as expected | ✅   |
| 6   | Number (guess)         | `7`                | Same message                                | as expected | ✅   |
| 7   | Multi-letter (guess)   | `xy`               | Same message                                | as expected | ✅   |
| 8   | Repeat guess           | same letter twice  | "You already guessed 'x'."                  | as expected | ✅   |
| 9   | Lowercase guess        | `a`                | Accepted, uppercased                        | as expected | ✅   |
| 10  | Correct guess          | letter in word     | Reveals letter, "Good guess!"               | as expected | ✅   |
| 11  | Wrong guess            | letter not in word | Lives drop by 1                             | as expected | ✅   |
| 12  | Win state              | guess all letters  | "You guessed the word..."                   | as expected | ✅   |
| 13  | Lose state             | 8 wrong guesses    | "Game over! The word was..."                | as expected | ✅   |
| 14  | Deployed app runs      | open live URL      | Game plays in browser terminal              | as expected | ✅   |
