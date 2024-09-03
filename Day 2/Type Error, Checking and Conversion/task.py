len("annoying")
#type allows us to check what kind of data type it is. we need to (wrap) and print for it to show
print(type("hello"))
print(type(123))
print(type(1.2))
print(type(False))

#converting data types
int("123")
#will convert string into numbers, for example
print(int("123") + int("456"))
#will actually treat the numbers in the string as numbers and add them rather than concatenate like a reg string

int()
float()
str()
bool()

#------------------------------------------------------------------------
#change this line of code to get it to run w/o errors
# -i managed to work backwards from the errors to figure out which types needed to be converted, the notes below
#  show the methodical way of checking types etc

#  print("Number of letters in your name: " + len(input("Enter your name")))

# assign variables to the working parts=
name_of_user = input("Enter your name")
length_of_name = len(name_of_user)

# figure out what the first part of the string's type is=
print(type("Number of letters in your name"))      #we find out after running that this is (str)
print(type(length_of_name))                        #we find out after running that this is (int)

#so convert int into a string---> "str(length of name)" or my solution below



print("Number of letters in your name: " + str(len(input("Enter your name: "))))