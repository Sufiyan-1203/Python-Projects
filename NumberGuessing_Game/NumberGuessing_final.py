import random

def get_difficulty():
    print("********** SELECT DIFFICULTY **********")
    print("1. Easy   (1 to 50,    10 guesses)")
    print("2. Medium (1 to 100,   7 guesses)")
    print("3. Hard   (1 to 200,   5 guesses)")
    print("****************************************")
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == '1':
            return 1, 50, 10
        elif choice == '2':
            return 1, 100, 7
        elif choice == '3':
            return 1, 200, 5
        else:
            print("Invalid input. Try again.")

def give_hint(secret, guess, prev_diff):
    diff = abs(secret - guess)
    if diff == 0:
        return "Correct!"
    if prev_diff is None:
        if diff <= 5:
            return ">> Very Hot!"
        elif diff <= 10:
            return ">> Hot"
        elif diff <= 20:
            return ">> Warm"
        elif diff <= 40:
            return ">> Cold"
        else:
            return ">> Very Cold"
    else:
        if diff < prev_diff:
            return ">> Getting hotter"
        elif diff > prev_diff:
            return ">> Getting colder"
        else:
            return ">> Same as last time"

def number_guessing_game():
    low, high, attempts = get_difficulty()
    secret_number = random.randint(low, high)
    previous_guesses = []
    prev_diff = None

    print("\n********** NUMBER GUESSING GAME **********")
    print(f"I have selected a number between {low} and {high}.")
    print(f"You have {attempts} chances to guess it!")
    print("*******************************************\n")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Guess {attempt}/{attempts}: "))
                if guess < low or guess > high:
                    print(f"Out of bounds! Enter a number between {low} and {high}.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number.")

        previous_guesses.append(guess)
        diff = abs(secret_number - guess)

        if guess == secret_number:
            print("\n****************** RESULT *******************")
            print(f"Correct! You guessed the number in {attempt} attempts.")
            print("***********************************************")
            break
        else:
            hint = give_hint(secret_number, guess, prev_diff)
            prev_diff = diff
            direction = "Try a higher number." if guess < secret_number else "Try a lower number."
            print(hint)
            print(f">> {direction}")
            print(f">> Previous guesses: {sorted(previous_guesses)}")
            print("*****************************\n")
    else:
        print("\n******************** GAME OVER ********************")
        print(f"You've used all attempts. The number was: {secret_number}")
        print("****************************************************")

number_guessing_game()
