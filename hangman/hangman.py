import random
words = ["apple", "grape", "mango", "peach", "berry"]
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
max_attempts = 6
attempts = 0

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while attempts < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Incorrect!")
        attempts += 1
        print(f"Remaining attempts: {max_attempts - attempts}")


if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game over! The word was:", word_to_guess)
