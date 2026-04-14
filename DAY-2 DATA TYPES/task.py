# #  Task 1 primitive data type

# # 1. strings
# # 2. integers
# # 3. float
# # 4. boolean

# #  To check the type of a data we use the type() function

# name = 'solomon'
# print(type(name)) # we get <class 'str'> as an output.

# # The method of pulling out a letter from a string is called Subscripting
# print("hello"[-1])

# # String 
# print("123"+"456")

# # Integer = whole numbers
# print(123 + 456)

# # Large Integers
# print(123_456_789) # we use the underscore(_) in representing large integers

# # Float = Floating Point Numbers
# print(3.141529)

# # Boolean
# print(True)
# print(False)









# # Task 2 Type Error, checking amd conversion

# # We can convert data types using builtin function for the desired data type ... e.g int(), str(), float(), bool()

# name_of_the_user = input("Enter Your Name")
# length_of_name = len(name_of_the_user)

# print("Number of letters in your Name " + str(length_of_name))








# # Task 3 Basic Operators, PEMDAS

# print(123+234) #Addition
# print(7-3) # Subtraction
# print(5*3) # Multiplication
# print(6/3) # Division
# print(5//3) # Floor Division 
# print(5**2) # Exponetial power

# # PEMDAS ... Parenthesis, Exponential, Multiplication, Addition and Subtraction.
# # This is the priority standard in carrying out Arithmetic operations in phython

# print(3*3+3/3-3) # This outputs 7.0

# print(3*(3+3)/3-3) # This outputs 3.0







# # Task 4 Number Manipulation

# num = 3.628399 

# print(int(num)) # This is called flooring, a process of removing all decimal numbers from a floating number.

# print(round(num)) # This is called,  where the digit is rounded to the nearest numbeer

# print(round(num, 2)) # This is rounding up to 2 decimal places. The round() function can take in two arguments, 
# # the first is the value and second is the number of decimal places to round up to.


# # keeping track of a value based on it's previous value.
# score = 0 

# # instead of writing score = score + 1 

# score += 1 #We can do this instead, same for decrement and others.


# # f-Strings
# print(f"Your Score is = {score}") # it enables us to easily insert various data into strings using curly braces {}



# Task 5 Tip Calculator Project

print ("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? "))
tip = int(input("How much Tip would you like to give? 10, 12, or 15? "))
payers = int(input("How many people are to split the bill? "))

total_bill = bill + tip
individual_bill = round(total_bill/payers, 2)

print(f"Each Person will pay {individual_bill}")