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
correct_guess = []
while not solved:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(letter)
        elif letter in correct_guess:
            display += letter
        elif letter != guess:
            display += "_"




    print(display)
    if display.find("_") == -1:
        solved = True
        print("You Win!")

###attempt 1. for some reason it's adding the outputs together when i guess more than one letter
# for example if the random word chosen is "aardvark" and I chose a, the output would be "aa___a__"
# onto the next step, choose another letter, r, and the output currently looks like "aa___a____r___r_"


## final attempt. couldn't figure it out and watched solution, pausing here and there to see if I could fix myself.
## the initial problem was that I had the display variable in the wrong place, outside of the while loop. that's why it
## continued to add to the end of the string "display"
## the other problem i was trying to fix was the infinite loop, even if i had guessed all the correct letters, it kept
## asking me to guess. it was an indentation issue, as well as i hadn't changed the variable "solved" to = True
## though the condition had been met.
## got stuck trying to figure out how to keep the correct guesses, and I think part of the reason I had a hard time coming up
## with the idea of creating another list was because stuck in the idea of trying to create a variable within the variable,
## but couldn't figure out how it would keep it when the loop starts again.
## also, when i googled how to check if a letter is in a string, i found the variable.find() rather than just using the
## IN keyword, so in a way I didn't learn how to search in a variable. The concept wasn't even on my radar.