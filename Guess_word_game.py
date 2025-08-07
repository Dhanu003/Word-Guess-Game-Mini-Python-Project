import random

# List of words to choose from
words = ["python", "java", "ruby", "html", "css"]

# Choose a random word
chosen_word = random.choice(words)

# Set the number of attempts
attempts = 3

# Game loop
print("Welcome to the Word Guess Game!")
print(f"Try to guess the word! You have {attempts} attempts.")

while attempts > 0:
    # User input
    guess = input("Enter your guess: ").lower()

    # Check if the guess is correct
    if guess == chosen_word:
        print("Congratulations! You've guessed the word correctly!")
        break
    else:
        attempts -= 1
        print(f"Oops! Wrong guess. You have {attempts} attempts left.")

# If the player runs out of attempts
if attempts == 0:
    print(f"Game over! The word was '{chosen_word}'.")
