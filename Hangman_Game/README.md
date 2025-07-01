# Hangman Game

## Overview
Hangman is a classic word-guessing game where players attempt to guess a hidden word by suggesting letters within a limited number of attempts. This Python implementation allows users to choose the length of the word they want to guess, making the game more customizable and engaging.

## Features
- Choose the length of the word (3 to 9 letters).
- Dynamic word selection based on user input.
- Visual representation of the hangman stages.
- Debug mode to display the chosen word for testing purposes.
- Tracks guessed letters to prevent duplicate guesses.
- Win or lose conditions based on lives remaining.

## Files
### 1. `hangman_final.py`
The main script that runs the Hangman game. It handles:
- User input for word length.
- Word selection and filtering.
- Game logic (guessing letters, updating the hidden word, tracking lives).

### 2. `hangman_words.py`
Contains a dictionary of word lists categorized by length (3 to 9 letters). Each list contains 100 words.

### 3. `hangman_art.py`
Contains the visual representation of the hangman stages and the game logo.

## How to Run
1. **Prerequisites**:
   - Python 3 installed on your system.

2. **Steps**:
   - Clone or download the project files into a directory.
     ```
   - Run the game using:
     ```bash
     python hangman_final.py
     ```

3. **Gameplay**:
   - Enter the desired length of the word (3 to 9).
   - Guess letters one at a time.
   - Win by guessing the word correctly or lose if you run out of lives.


## Example Output

Enter the desired length of the word (3 to 9): 4

Word to guess: ____

**************************** 6/6 LIVES LEFT ****************************

Guess a letter: a

'a' is not in the word. You lose a life.

Word to guess: ____

**************************** 5/6 LIVES LEFT ****************************

Guess a letter:




## Customization
- Add more words to [hangman_words.py] to expand the word pool.
- Modify [hangman_art.py] to customize the hangman stages or logo.

## License
This project is open-source and free to use.

## Author
Created by **MOHAMMED SUFIYAN ALI**.

Enjoy playing Hangman!
