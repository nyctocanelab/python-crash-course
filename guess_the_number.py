import random

NUMBER_OF_GUESSES = 10
print("Welcome to the Guess the Number Game!")
computer_selected_number = random.randint(1, 100)

for attempt in range(NUMBER_OF_GUESSES):
    try:
        user_selected_number = int(input(f"Attempt {attempt+1}/{NUMBER_OF_GUESSES}: Enter a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if user_selected_number < computer_selected_number:
        print("Too low!")
    elif user_selected_number > computer_selected_number:
        print("Too high!")
    else:
        print("You guessed it right!")
        break
else:
    print(f"You have exhausted all your guesses. The number was {computer_selected_number}")
