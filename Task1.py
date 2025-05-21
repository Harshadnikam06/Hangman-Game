import random

# List of possible words
word_list = ["python", "hangman", "developer", "programming", "keyboard", "laptop", "algorithm"]

# Select a random word from the list
word = random.choice(word_list).lower()
guessed_letters = []
attempts = 6  # Number of allowed wrong guesses

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

print("🎮 Welcome to Hangman Game!")
print("You have", attempts, "incorrect guesses allowed.")

# Game loop
while attempts > 0:
    print("\nWord:", display_word(word, guessed_letters))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:a
        attempts -= 1
        print("❌ Incorrect guess. Attempts left:", attempts)

else:
    print("\n💀 Game Over! The word was:", word)
