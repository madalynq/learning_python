import random
import hangman_words              ###two ways to import either this and line #5
from hangman_art import stages, logo    ### or this and skip 5
hangman_words.word_list

lives = 6

print(logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}.")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter
        elif letter not in correct_letters:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*****Correct Answer Was: {chosen_word.upper()}! ****YOU LOSE**********************")
    elif guess in display:
        lives += 0
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
