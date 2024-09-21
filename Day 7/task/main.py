import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
solved = False
display = ""
while not solved:
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
if display.find("_") == -1:
    print("You Win!")

###attempt 1. for some reason it's adding the outputs together when i guess more than one letter
# for example if the random word chosen is "aardvark" and I chose a, the output would be "aa___a__"
# onto the next step, choose another letter, r, and the output currently looks like "aa___a____r___r_"
