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

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose!")
            break
    
    print(f"{' '.join(display)}")
    from hangman_art import stages
    print(stages[lives])

if "_" not in display:
    print("Congratulations! You have won!")
