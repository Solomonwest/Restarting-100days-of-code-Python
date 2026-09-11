
#                                   TASK 1
# 
# WHAT IS A FUNCTION IN PYTHON ?

# A function is a block of statements / code that is only executed when called.

# To create a function we use the keyword "def" which means define and a parenthesis '()'.
# 
# example  
# 
# def my_function():
#    statements

# All statements for the function must be properly indented inside the fuction.
# We call a fuction with it's name and the parenthesis
# 
# example 
# 
# my_function() ---- then the statements inside the function will be executed.

# when we run this code the it prints out -- "How's thw weather today in Kaduna?"
def greet():
    print("How's the weather today in Kaduna?")

greet()


# FUNCTIONS WITH INPUTS
# 
# If you wondered if the parenthesis in a function are being used ... yes you're right.
# They are used to pass input into the fuction, so the fuction can make use of that input.

def name_function(name):
    print(f"Hi {name}, how do you do?")

name_function("Stephen")

# The variable "name" inside the function is called a Parameter
# 
# The data "Stephen" passed in the parenthesis when calling the function is referred to as an Argument (Args)
# 
# In other words the Parameter 'name' in the function is a variable that holds the data (Argument) entered during function call, so the above code will print 
# Hi Stephen, how do you do?

# You can also add multiple arguments to a function using a comma 
# 
# example

# both name and age are added to the profile function
def profile(name, age):
    print(f"I'm {name} and i am {age} years old.")

profile("Peach", 22)

