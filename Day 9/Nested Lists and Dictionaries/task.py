capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary:

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# #print Lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

#print D
print(nested_list[2][1])

#dictionary in dictionary

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },
}

#how to print Stuttgart:
print(travel_log["Germany"]["cities_visited"][0])