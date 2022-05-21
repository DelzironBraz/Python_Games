from words import words
import string
import random

def is_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = is_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_letters)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Type a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You already tried this one")

        else:
            print("Invalid character")

    print(f"You guessed {word}")

hangman()
