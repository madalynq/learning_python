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

##love calculator exercise:
#enter two people's names, take the number of times the letters in TRUE appear in both names, and LOVE.
#concatonate numbers to get love score

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)

calculate_love_score("kanye west","kim kardashian")