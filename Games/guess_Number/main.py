import random

n = random.randint(1, 100)
a = -1
guesses = 0

while(a != n):
    guesses += 1

    a = int(input("Guess the number: "))

    if(a > n):
        print("guess a lower number please ⏪!!")
    else:
        print("guess a higher number please ⏩!!")

print(f"You have guessed the right number{n} correctly in {guesses} attempts😊")

import random

n = random.randint(1, 100)
guesses = 0

while True:
    try:
        a = int(input("Guess the number: "))
        guesses += 1

        if a > n:
            print("Guess a lower number ⏪!!")
        elif a < n:
            print("Guess a higher number ⏩!!")
        else:
            print(f"🎉 You guessed the right number {n} in {guesses} attempts! 😊")
            break
    except ValueError:
        print("⚠️ Please enter a valid number!")


import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts}. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            break
    
    if attempts >= max_attempts and guess != secret_number:
        print(f"\nGame over! You've used all {max_attempts} attempts.")
        print(f"The secret number was {secret_number}.")

    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
guess_the_number()