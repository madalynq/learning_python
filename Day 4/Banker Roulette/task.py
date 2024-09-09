friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
randomizer = random.randint(1,5)
if randomizer == 1:
    print(friends[0])
elif randomizer == 2:
    print(friends[1])
elif randomizer == 3:
    print(friends[2])
elif randomizer == 4:
    print(friends[3])
else:
    print(friends[4])
