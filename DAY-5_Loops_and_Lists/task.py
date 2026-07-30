# Task 1 For Loops -- Executing the same statement multiple times

fruits = ["Strawberry", "Peach", "Mango", "Apple"]

for fruit in fruits:
    print(fruit)



# Task 2 - High Score and Sum score

# we can use the sum keyword to add numbers that can be iterated.
# we can use the max keyword to get the maximum value amongst iterable numbers.

student_score = [30,49,28,94,92,39,83,90,71,27,105]

# Add the total numbers in the list
sum = 0
for score in student_score:
    sum +=score

print(sum)


# Get the highest value of the list
max_value = 0
for score in student_score:
    if score > max_value:
        max_value = score

print(max_value)


# Task 3 - for loops with the Range function

# This prints all numbers from 1 to 9
# it doesn't include the last value of the range.
for num in range(1, 11):
    print(num)

# Range step size is the 3rd Argument applied to the range 
# The step size is the number of value to be skipped before displaying the next sequence
for num in range(1, 30, 2):
    print(num)
