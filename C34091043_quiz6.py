import random

def print_histogram(guesses):
    print("\nGuess histogram:")
    for i in range(len(guesses)//4 + 1):
        print(" ".join(guesses[i*4:i*4+4]))

lowercase_alphabet = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(lowercase_alphabet)
answer = lowercase_alphabet.pop()

guesses = []
num_attempts = 0

while True:
    guess = input("Guess the lowercase alphabet: ").lower()  # 將輸入轉換為小寫

    if len(guess) != 1 or not 'a' <= guess <= 'z':
        print("Please enter a single lowercase alphabet character.")
        continue

    num_attempts += 1
    guesses.append(guess)

    if guess == answer:
        print(f"Congratulations! You guessed the alphabet '{answer}' correctly in {num_attempts} attempts.")
        print("Previous guesses:", " ".join(guesses))
        print_histogram(guesses)
        break
    elif ord(guess) < ord(answer):
        print("Too low!")
    else:
        print("Too high!")