#range


#range(1,10)
###if you try to print this, it doesnt do anything, it needs to be used in conjunction with something else

#for number in range(1,10):
   # print(number)            ###this will print numbers 1-9, not including 10. if you want to include the number 10,
                              ### increase the range, (1, 11)
                              ### by default, the range will print every variable, increasing by 1.(so it will print,
                              ### "1,2,3,4,5,6,7,8,9,10" as each individual variables.
                              ### if you want it to increase by any other number, you add that number after the range,
                              ### in the parenthesis ----> (1,11,3)
for number in range(1,11,3):
    print(number)             ### this will print variables increasing by 3, so "1,4,7,10" as individual variables

print(sum(range(1,101)))

### OR ###

total = 0
for number1 in range(1, 101):
    total += number1
print(total)
