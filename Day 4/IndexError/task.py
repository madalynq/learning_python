

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
#if you try to get an item that is not in the range of a list, you will get an IndexError
#print(states_of_america[50]) ###"list index is out of range" because there are 50 states but lists start with 0, not 1

#Nested lists

fruits = ["cherry", "strawberry", "apple", "orange", "mango"]
vegetables = ["carrot", "broccoli", "cabbage", "peppers"]
fruits_and_vegetables = [fruits, vegetables]
print(fruits_and_vegetables)
# should look like: [['cherry', 'strawberry', 'apple', 'orange', 'mango'], ['carrot', 'broccoli', 'cabbage', 'peppers']]
##double brackets to show the list includes more than one list