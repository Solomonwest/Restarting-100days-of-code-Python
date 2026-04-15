# # TASK 1 -----   IF ELSE

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
