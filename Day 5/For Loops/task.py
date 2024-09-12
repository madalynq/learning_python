fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit) ##will print each variable individually
    print(fruit + " pie") ## prints for each variable, but each step of code under an if must be carried out in
                          ## order. the previous step called for each variable to be printed individually, and code will
                          ## take care of everything needed (code) for that specific variable before moving onto the
                          ## next variable
    print(fruits)         ######indentation matters. if this is under an if, it will be printed for every variable
    print("every variable")
print("BACK TO NORMAL")   ### when you're no longer in the indentation under the if, it goes back no normal code
                          ## loop is ended and its back to regular code
