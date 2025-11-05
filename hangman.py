import random
import time

# Ensure a different random word each time
random.seed(time.time())

# Predefined list of words
words = ["python", "computer", "engineer", "database", "program"]

# Randomly select a word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []
wrong_letters = []

print("🎯 Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.")
print("Word to guess:", " ".join(guessed_word))

# Main game loop
while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        wrong_letters.append(guess)
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed_word))
    if wrong_letters:
        print("Wrong guesses so far:", ", ".join(wrong_letters))

# Check win/loss condition
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)