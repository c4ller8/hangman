![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Hangman

A command-line Hangman game built in Python. The player picks a starting
letter (A–Z), then guesses letters to reveal a hidden word before running
out of lives.

**Live deployed app:** https://hangman-c4ller8-28c30dbca314.herokuapp.com

---

## Purpose

Hangman is a classic word-guessing game. This project implements it as a
terminal application, giving the user a quick, replayable game that runs
in any Python environment.

## Value to the user

- Simple, familiar game — no learning curve
- Choose your category by picking a starting letter (A–Z)
- Immediate feedback on every guess
- Handles invalid input gracefully (empty, numbers, repeats, wrong length)

## How to play

1. Pick a starting letter (A–Z) to choose a word category.
2. Guess one letter at a time.
3. Correct guesses reveal the letter's position(s) in the word.
4. Wrong guesses cost one of your 8 lives.
5. Win by revealing the whole word. Lose by using all 8 lives.

## How to run locally

1. Ensure Python 3 is installed.
2. Clone this repository.
3. In the project folder, run: python3 run.py
4. Follow the on-screen prompts.

## Features

- Category selection by starting letter (uses a dict of words grouped A–Z)
- 8 lives per game
- Live display of lives remaining, used letters, and current word state
- Input validation for empty, multi-character, non-letter, and repeat guesses
- Exception handling around input (catches closed input / EOF)
- Win and lose end states with the word revealed

## Data model

Words are stored in `words.py` as a dictionary, `words_per_letter`, keyed
by starting letter:

```python
words_per_letter = {
    'A': ['apple', 'amber', 'angel', 'attic', 'agile', 'alarm'],
    'B': ['bacon', 'badge', 'bagel', 'baker', 'balmy', 'banjo', 'barge'],
    ...
}
```

This lets the player choose a category before playing, and gives the game
a real structure to query and select from.

## Project structure

| File               | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| `run.py`           | Main game — entry point, all game logic            |
| `words.py`         | Word data, grouped by starting letter              |
| `requirements.txt` | Python dependencies (none — standard library only) |
| `README.md`        | This file                                          |
| `TESTING.md`       | Manual testing evidence                            |

## Testing

See [TESTING.md](TESTING.md) for the full manual testing table.

Summary: all tested inputs — empty, numbers, multi-letter, repeats,
lowercase, win state, lose state — behave as expected.

## Deployment

Deployed to Heroku using the Code Institute student template.

- **Heroku app:** hangman-c4ller8
- **Live URL:** https://hangman-c4ller8-28c30dbca314.herokuapp.com
- **Buildpacks (in order):** `heroku/python`, `heroku/nodejs`
- **Config Var:** `PORT` = `8000`

## Constraints

The deployment terminal is set to 80 columns by 24 rows. All lines of
output have been kept within 80 characters.

## Credits

- Code structure inspired by "12 Python Beginner Projects" (YouTube)
- Word list created for this project
- Code Institute student template for deployment structure

```

```
