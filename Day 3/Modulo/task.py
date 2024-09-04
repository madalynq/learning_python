# modulo is not a division, it calculates the remainders left after the division
#10/ 2 = 5, no remainders,                so 10 % 2 = 0
#10/ 3 = 3.333333 or 3 with 1 remaining.  so, 10 % 3 = 1

#even_number 12 % 2 == 0

modulo = int(input("Check number: "))

if modulo % 2 == 0:
    print("Even")

else:
    print("Odd")

