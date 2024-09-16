def my_function():
    print("hello")
    print("bye")

my_function()      ####"calling" the function


### this allows a block of code to all be carried out at once. shorthand, in a way. calling a function can simplify code
### rather than typing each individual step out

### creating code for Reeborg's world, challenge is to get the robot to turn right when there is no "right turn" in
### the code, create a function that carries out the process.


# def turn_right():
#   turn_left()
#   turn_left()
#   turn_left()
# turn_right()


#created a "jump" function:

# def jump():
#   move()
#   turn_left()
#   move()
#   turn_right()
#   move()
#   turn_right()
#   move()
#   turn_left()

### challenge was to make the robot jump a hurdle, 6 times. and to simplify code as much as possible.(loops)

### for hurdle in range(0,6):
###     jump()

########## INDENTATION IS IMPORTANT #########


#### while loops ####

#another way to simplify this code is to use a different kind of loop, a while loop. a while loop will continue
#loooping through code until a condition has been met.
# ex//     while something_is_true:
#              do this
#              do this

#ex// instead of "for hurdle in range" loop above, create a variable to create condition, and then create while loop:

#number_of_hurdles = 6
#while number_of_hurdles > 0:
#   jump()
#   number_of_hurdles -= 1       -----> included in the loop, so that it will keep track of how many turns are left
#                                -----> when the condition is met, or the number of hurdles is 0 (not >0), it will
#                                -----> stop running the code for the loop

#next challenge was to get the robot to keep jumping until it reached a randomized finish line.
# ----> condition given: at_goal()

#while at_goal() != True:           ---->another way of saying this in code: while not at_goal():
#   jump()                           -----> however this flips the logic. while NOT at_goal would continue as a true
#                                    -----> statement, and stop running the loop when the condition becomes false
#                                    -----> or, when it reaches at_goal it becomes false because it is no longer NOT_at_goal
#the code above is saying,
# while at_goal is not equal to true (so it's false)
# keep running loop. when it IS equal to true, the loop
# stops as its condition has been met


## while loops continue running until conditions have been met. infinite loops can be created, be careful of that.
## for loops and loops with range are better for lists that need something specific done to each variable, while loops
## are better for when you don't care too much about the numbers of the sequence and when you just need the console to
## continue repeating a function for you until you reach a condition that you've set.
## while loops are better for repeating functions
## for loops are better for precision


#### you can nest within loops.
# while at_goal() != True:
#     if wall_in_front() == TrueL
#         jump()
#     elif front_is_clear():
#         move()