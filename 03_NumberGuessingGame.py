import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too Low! Try again.")
        elif user_guess > number_to_guess:
            print("Too High! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# Call the game function
number_guessing_game()
