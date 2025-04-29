import random

def number_guessing_game():
    numbers = [1, 5, 12, 20, 25, 32, 42, 50, 60, 75]
    secret_number = random.choice(numbers)
    
    print("Welcome to the Number Guessing Game!")
    print("I've chosen a number from the list. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Guess higher.")
        else:
            print("Too high! Guess lower.")

if __name__ == "__main__":
    number_guessing_game()