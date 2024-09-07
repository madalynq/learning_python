print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_turn = input("At the center of this island is a giant hedge maze. Upon entering the maze, you can either turn left, or right. Which do you choose?\n")
if first_turn in ["right", "Right", "R", "r", "RIGHT"]:
    print("You wind through a seemingly endless maze for hours, which also somehow seems to be taking you uphill.\n You reach a clearing just as the sun sets, and you can barely make out a door at the far end of the clearing.\n Desperate to reach the end, you run to the door, yank it open, step through... \n And find yourself falling down the side of a sandy cliff, bringing you right back to where you started on the island. \n GAME OVER")
elif first_turn in ["left", "Left", "L", "l", "LEFT"]:
    second_turn = input("Turning left, you follow a dimly lit path that winds to the other end of the island.\n You find yourself on a small beach surrounded by cliffs, and you can see another small island out across the water.\n Judging the distance, you think that you can make the swim in about 30 minutes, but the sun is setting and you think you've got maybe 20 minutes of daylight left.\n You can either make the swim, or wait for morning.\n  Do you swim, or wait?\n")
    if second_turn in ["swim", "Swim", "SWIM", "S", "s"]:
        print("Your try your luck, as you know you're a strong swimmer.\n About 15 min into your swim, as the daylight is fading, angry storm clouds quickly cover the sky.\n Between the wind, waves as tall as skyscrapers, the rain and the lightning, you can no longer tell where land is.\n GAME OVER")
    elif second_turn in ["wait", "WAIT", "Wait", "W", "w"]:
        third_turn = input("You decide to wait for morning, when there will be more light and you will be more rested.\n You set up camp in a cave in the cliff side, and as night falls, a storm rolls in.\n Safe in the cave, you awake in the morning to a calm and peaceful ocean, with the tide pulled back so far that you can walk to the small island you saw the night before.\n You make your way to the little island and find three small houses, all with different color doors: Blue, Red, and Yellow.\n Which door do you choose?\n ")
        if third_turn in ["red", "RED", "Red","R", "r"]:
            print("You open the red door, trip on on the uneven doorway, and fall forward.\n The falling sensation wakes you up and you realize the whole thing was a dream.\n GAME OVER")
        elif third_turn in ["blue", "BLUE", "Blue", "B", "b"]:
            print("As you open the blue door, a trapdoor under your feet opens and you fall into a pit of spikes.\n GAME OVER")
        elif third_turn in ["yellow", "YELLOW", "Yellow", "Y", "y"]:
            print("You open the yellow door to find an abandoned room with nothing but a stove in the corner.\n You open the stove and find it stuffed with gold bars.\n YOU WIN!!!")
        else:
            print("Invalid input, GAME OVER")
    else:
        print("Invalid input, GAME OVER")
else:
    print("Invalid input, GAME OVER")