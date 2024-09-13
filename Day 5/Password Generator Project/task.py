import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for letter in range(0, nr_letters):
    qwe = random.choice(letters)
    password += qwe

for number in range(0,nr_numbers):
    rty = random.choice(numbers)
    password += rty

for symbol in range(0, nr_symbols):
    uio = random.choice(symbols)
    password += uio

print(password)

### to simplify code, forgo creating a variable/ adding variable to password:
###     for letter in range(0, nr_letters):
###         password += random.choice(letters)
###

hard = list(password)    ###this is converting the sting (password) into a list (hard)
print(hard)              ###printing to make sure it's working
random.shuffle(hard)     ###this is shuffling the order of the list
print(hard)              ### printing to make sure it's working

password2 =""            ###converting back to a string
for char in hard:        ### give the variables in list (hard) a name                -----char, short for character---
    password2 += char    ### add each variable together to a string in (password2)



print(f"Your password could be:{password2}")



##### the way shown in the video is to copy all the code for the "easy" version and paste below, make password22
##### a list straight away instead of a string. continue to add variables to a list rather than string.

#####password22 = []

#####for letter in range(0, nr_letters):
#####   qwe = random.choice(letters)
#####    password22.append(qwe)

#####for number in range(0,nr_numbers):
#####    rty = random.choice(numbers)
#####    password22.append(rty)

#####for symbol in range(0, nr_symbols):
#####    uio = random.choice(symbols)
#####    password22.append(uio)

#####print(password22)            ----> make sure it's printing the right thing
#####random.shuffle(password22)   ---->shuffle list
#####print(password22)            ----> make sure it shuffles list

#####password3 = ""               ----> converting list(password22) back to string(password3)
#####for char in password22:      ----> give variables in list(password22) a name
#####   password3 += char         ----> add each variable together in string(password3)

#####print(f"Your password is: {password3}")