# TASK 1 -----   IF ELSE

print("Welcome to the rollercoaster! ")
height = float(input("what is your height in cm? "))

if height >= 120:
    print("You're legal and can ride..")
else:
    print("Sorry you're not eligle for. the ride.")


# Task 2 --------- Modulo Operator

# The modular operation is used to perform a division and gives the reaminder after the division.

# challenge... 
# CHECK IF THE NUMBER ENTERED BY THE USER IS AN ODD OR AN EVEN NUMBER


number = int(input("Enter any whole number of your choice: "))

if number % 2 == 0:
    print('This is an Even Number!')
else:
    print("This is an Odd Number!")



# # # TASK 3 -----  NESTED IF/ELSE, ELIF

# This is used when we want multiple conditions in one condition

print("Welcome to the rollercoaster! ")
height = float(input("what is your height in cm? "))

if height >= 120:
    print("You're legal and can ride..")
    age = int(input("Enter Your Age: "))
    if age < 12:
        print("Your Bill is $5")
    elif age <= 18:
        print("Your Bill is $7")
    else:
        print("Your Bill is $12")
else:
    print("Sorry you're not eligle for. the ride.")