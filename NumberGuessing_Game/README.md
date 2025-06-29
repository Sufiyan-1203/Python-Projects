# Number Guessing Game

## Overview
This is a simple and interactive Number Guessing Game written in Python. The player selects a difficulty level, and the program randomly chooses a number within a specified range. The player must guess the number within a limited number of attempts, receiving hints after each guess.

## Features
- Three difficulty levels: Easy, Medium, Hard
- Hints provided after each guess (hot/cold and getting hotter/colder)
- Tracks and displays previous guesses
- Input validation for guesses and difficulty selection

## How to Play
1. **Select Difficulty:**  
   Choose from Easy (1-50, 10 guesses), Medium (1-100, 7 guesses), or Hard (1-200, 5 guesses).

2. **Guess the Number:**  
   Enter your guess. The game will tell you if you are getting "hotter" or "colder" compared to your previous guess, and whether you should try a higher or lower number.

3. **Win or Lose:**  
   Guess the number within the allowed attempts to win. If you run out of attempts, the correct number is revealed.

## How to Run

1. Make sure you have Python 3 installed.
2. Place `NumberGuessing_final.py` in your working directory.
3. Open a terminal and navigate to the directory:
   ```bash
   cd c:\Users\SUFIYAN\OneDrive\Desktop\Python Projects\NumberGuessing_Game
4. Run the script:
   python NumberGuessing_final.py

## Example Output

********** SELECT DIFFICULTY **********
1. Easy   (1 to 50,    10 guesses)
2. Medium (1 to 100,   7 guesses)
3. Hard   (1 to 200,   5 guesses)
****************************************
Enter 1, 2 or 3: 2

********** NUMBER GUESSING GAME **********
I have selected a number between 1 and 100.
You have 7 chances to guess it!
*******************************************

Guess 1/7: 50
>> Warm
>> Try a higher number.
>> Previous guesses: [50]
*****************************

...
****************** RESULT *******************
Correct! You guessed the number in 4 attempts.
***********************************************

## License
This project is open-source and free to use.

## Author
Created by **MOHAMMED SUFIYAN ALI**.

Enjoy playing!