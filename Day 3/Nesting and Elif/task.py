print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age <= 12:
        print("$5 please")
    elif age <=18:
        print("$7 please")
    else:
        print("$12 please")
else:
    print("Sorry you have to grow taller before you can ride.")


concession = int(input("After the rollercoaster, would you like to try visit our concession stand? 1 for yes, 2 or no "))

if concession == 1:
    Food = int(input("Choose 1 for Hamburger meal, choose 2 for Funnel cake, choose 3 for Cotton Candy "))
    if Food == 1:
        print("Thank you for choosing the Hamburger meal, $12 please")
    elif Food == 2:
        print("Thank you for choosing Funnel cake, $10 please")
    else:
        print("Thank you for choosing Cotton Candy, $4 please")
else:
    print("Thank you for riding our rollercoaster today, enjoy your ride!")