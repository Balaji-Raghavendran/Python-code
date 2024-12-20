import random

def number_find_game():
    print("Welcome to the Number Find Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            print("Attempt " + str(attempts + 1) + "/" + str(max_attempts) + ": Enter your guess: ")
            guess = int(input())
            attempts += 1
            
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed it in " + str(attempts) + " attempts.")
                return
        except ValueError:
            print("Enter a valid number.")
    
    print("Out of attempts! The number was " + str(target_number) + ".")

number_find_game()