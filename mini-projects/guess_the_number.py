import random

def guess_number():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")

# Run the game
guess_number()
