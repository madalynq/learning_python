rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)


import random
comp_choice = random.randint(0,2)
if comp_choice == 0:
    print(f"Computer chose:\n {rock}")
elif comp_choice == 1:
    print(f"Computer chose:\n {paper}")
else:
    print(f"Computer chose:\n {scissors}")


if user_choice == 0 and comp_choice == 0:
    print("Draw")
elif user_choice == 0 and comp_choice == 1:
    print("You Lose")
elif user_choice == 0 and comp_choice == 2:
    print("You Win")
elif user_choice == 1 and comp_choice == 0:
    print("You Win")
elif user_choice == 1 and comp_choice == 1:
    print("Draw")
elif user_choice == 1 and comp_choice == 2:
    print("You Lose")
elif user_choice == 2 and comp_choice == 0:
    print("You Lose")
elif user_choice == 2 and comp_choice == 1:
    print("You Win")
elif user_choice == 2 and comp_choice == 2:
    print("Draw")

##### i came up with this first, but it wasn't printing. i tried to run the code above and it also wasn't working.
##### turns out i was forgetting to turn the user_input into an integer.

if user_choice == 0:
    if comp_choice == 0:
        print("Draw")
    elif comp_choice == 1:
        print("You Lose")
    else:
        print("You Win")
elif user_choice == 1:
    if comp_choice == 0:
        print("You Win")
    elif comp_choice == 1:
        print("Draw")
    else:
        print("You Lose")
elif user_choice == 2:
    if comp_choice == 0:
        print("You Lose")
    elif comp_choice == 1:
        print("You Win")
    else:
        print("Draw")
