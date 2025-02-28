import random

from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

from hangman_art import logo
print(logo)

print(f"Pssst, the solution is {chosen_word}.")

display = []

for letter in chosen_word:
    display.append("_")