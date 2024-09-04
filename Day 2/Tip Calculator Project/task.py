print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip2 = tip /100 + 1.0


total = bill * tip2 / people
total2 = round(total, 2)

print(f"Each person should pay: ", total2)




#this is what was given in the solution:
#bill_with_tip = tip / 100 * bill + bill
#print(bill_with_tip)