# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
repeat = False
users_dictionary = {}

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    #could have used max function
    #max(users_dictionary, key=users_dictionary.get)
    for person in bidding_dictionary:
        bid_amount = bidding_dictionary[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not repeat:
    name = input("What is your name? ").title()
    bid = int(input("What is your bid? $ "))
    users_dictionary[name] = bid
    others = input("Are there any others who would like to place a bid? (y/n) ")
    if others.lower() == "y":
        print("\n" * 20)
    elif others.lower() == "n":
        repeat = True
        find_highest_bidder(users_dictionary)



#




