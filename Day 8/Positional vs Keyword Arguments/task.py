# Functions with multiple inputs

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}?")


greet_with_name("Jack Bauer", "New York")
##positional arguments: the order you put the arguments in matter, the argument is assigned to the variables, or parameters
## in order of placement in the function


##keyword arguments: specify which is which in the function
greet_with_name(location="New York", name="Jack Bauer")