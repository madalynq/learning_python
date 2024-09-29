def greet():
    print("Hello!")
    print("Thanks for choosing Your MarketStreet Albertson's bakery.")
    print("What can I do for you today?")

greet()
#### you can put variables in the functions
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do, {name}?")
###if you try to call the function, it's going to ask you to input in the parenthesis so it can put it in the function
greet_with_name("Madalyn")

##the variable being placed in the parenthesis is called a parameter (ex// the variable "name" placed in the function
##is the parameter) NAME OF DATA
##what the variable puts out is the argument (ex//placing "madalyn" in the function when calling it is the argument)
##ACTUAL VALUE OF DATA