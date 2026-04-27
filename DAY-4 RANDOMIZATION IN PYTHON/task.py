import random


# Task 1 Random Module

# Random integers 
random_integer = random.randint(0, 10)
print(random_integer)


# Random floating numbers

random_from_0_to_1 = random.random()
print(random_from_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)


# Heads and Tails Randomization
test_case = random.randint(0,1)

print(test_case)
if test_case == 0:
    print("Heads")
else:
    print("Tails")