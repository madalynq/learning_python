programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#print(programming_dictionary)

#adding to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

empty_dictionary = {}


#wipe an existing dictionary
#programming_dictionary = {}

#edit existing value
#if there is no key that matches, it will add a new one
programming_dictionary["Bug"] = "A moth in your computer"

#loop through dictionary
for thing in programming_dictionary:
    print(thing)
    #only prints keys, should put 'for key in dictionary'
    print(programming_dictionary[thing])
    #will include values