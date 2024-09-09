# lists
# items in lists are listed in an order, lists are numbered starting at zero. so the first item in the list is number 0.
states_of_america = ["Delaware","Connecticut"]
#to find a specific thing in a list:
print(states_of_america[1]) ## the answer will be Connecticut, because Delaware is item 0
##you can also use negative numbers to find things on a list, and count backwards from the end of the list

#to change items in the list, you call the item number in the variable and then change it
states_of_america[0] = "Delerware"

print(states_of_america[0])

##add to the list:
states_of_america.append("Disneyland")
print(states_of_america)

##add more than one item:
states_of_america.extend(["Universal Studios", "Six FLags", "Hershey's"])
print(states_of_america)