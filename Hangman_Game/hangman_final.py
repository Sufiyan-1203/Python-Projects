import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
game_over = False
correct_guesses = []

print(logo)
print()
while True:
    try:
        word_length = int(input("Enter the desired length of the word (3 to 9): "))
        if 3 <= word_length <= 9:
            break
        else:
            print("Please enter a number between 3 and 9.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

filtered_words = word_list.get(word_length, [])

chosen_word = random.choice(filtered_words)

hidden_word = "_" * len(chosen_word)
print(f"Word to guess: {hidden_word}")

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_guesses:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    updated_word = ""
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            updated_word += letter
        elif hidden_word[index] != "_":
            updated_word += letter
        else:
            updated_word += "_"

    if guess in chosen_word:
        correct_guesses.append(guess)
        hidden_word = updated_word
        print(f"Word to guess: {hidden_word}")
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")
        print(f"Word to guess: {hidden_word}")

    if lives == 0:
        game_over = True
        print(f"*********************** GAME OVER! The word was '{chosen_word}'. ***********************")
    elif "_" not in hidden_word:
        game_over = True
        print("**************************** YOU WIN! ****************************")

    print(stages[lives])