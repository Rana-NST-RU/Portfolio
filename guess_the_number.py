import random

def guess_the_number():
    lower_bound = 1
    upper_bound = 100
A
    number_to_guess = random.randint(lower_bound, upper_bound)

    print("Welcome to the 'Guess the Number' Game!")
    print(f"Guess a number between {lower_bound} and {upper_bound}.")

    attempts = 0

    while True:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if player_guess < number_to_guess:
            print("Too low! Try again.")
        elif player_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts!")
            break  

guess_the_number()
