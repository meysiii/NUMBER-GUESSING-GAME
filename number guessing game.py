import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("I have selected a number between 1 and 50.")
    print("Can you guess it?")

    # Generate random number
    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Try again.\n")
            elif guess > secret_number:
                print("Too High! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts! 🎉")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!\n")

    # Replay option
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
