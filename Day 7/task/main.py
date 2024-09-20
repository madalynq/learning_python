import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess1 = input("Choose a letter:\n").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
word_divided = list(chosen_word) ##I converted to a list because I forgot that for loops can cycle through strings
for letter in word_divided:
    if guess1 == letter:
        print("right")
    else:
        print("wrong")
