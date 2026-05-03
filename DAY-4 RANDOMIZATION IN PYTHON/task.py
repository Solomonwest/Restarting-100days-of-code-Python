# import random


# # Task 1 Random Module

# # Random integers 
# random_integer = random.randint(0, 10)
# print(random_integer)


# # Random floating numbers

# random_from_0_to_1 = random.random()
# print(random_from_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)


# # Heads and Tails Randomization
# test_case = random.randint(0,1)

# print(test_case)
# if test_case == 0:
#     print("Heads")
# else:
#     print("Tails")



# # Task 2 Python Lists

# # data in the list are stored in index
# states_of_nigeria = ["Abuja", "Lagos", "Kwara"]

# # Change the data in a a list
# states_of_nigeria[1] = 'Osun'

# # Add an item at the end of the list.
# states_of_nigeria.append('Kogi')

# print(states_of_nigeria)


# # Task 3 Who will pay the Bill?

# friends = ['daniel', 'donald', 'malem', 'nicholas', 'david']

# total_friends = len(friends)

# rand_friend = random.randint(0, total_friends-1)

# # This prints out random friends from the list of friends.
# print(friends[rand_friend])



# # Task 4 Index Error

# # This error shows when the index of a list requested is out of range.
# #  The best way to handle that is to get the length of the list and subtract 1 from it.  e.g  

# num_of_states = len(states_of_nigeria)

# # with this we get the last data in the list
# print(states_of_nigeria[num_of_states-1])


# Task 5  Nested List
#  Having a List inside a list 
vegetables = ['tomato', 'lettuce', 'cabbage', 'onions', 'onion']

fruits = ['Apple', 'Guava', 'strawberry', 'pineaple']

store = [vegetables, fruits]

print(store[1])


