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



# Task 2 Python Lists

# data in the list are stored in index
states_of_nigeria = ["Abuja", "Lagos", "Kwara"]

# Change the data in a a list
states_of_nigeria[1] = 'Osun'

# Add an item at the end of the list.
states_of_nigeria.append('Kogi')

print(states_of_nigeria)