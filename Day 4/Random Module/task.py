import random
import my_module


random_integer = random.randint(1,10)
print(random_integer)

print(my_module.my_favorite_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)


if random_integer >= 6:
    print("Heads")
else:
    print("Tails")
