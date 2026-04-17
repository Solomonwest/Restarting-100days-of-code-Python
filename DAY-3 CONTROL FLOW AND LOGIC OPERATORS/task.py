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



# TASK 3 -----  NESTED IF/ELSE, ELIF

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




# TASK 4 -----  MULTIPLE IF STATEMENTS

# This is used when we want to perform multiple actions, when multiple conditions are true... unlike the nested IF/ELSE, ELIF


print("Welcome to the rollercoaster! ")
height = float(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("You're legal and can ride..")
    age = int(input("Enter Your Age: "))
    if age < 12:
        bill = 5
        print("Your Bill is $5")
    elif age <= 18:
        bill = 7
        print("Your Bill is $7")
    else:
        bill = 12
        print("Your Bill is $12")
    wants_photo = input("Do you want to have a photo? type 'y' for Yes and 'n' for No: ")

    if wants_photo == 'y':
        bill += 3
        print(f"Your final bill is ${bill}, Have a great ride. ")
    elif wants_photo == 'n':
        print(f"Your bill remains {bill}, Enjoy your ride.")
    else:
        print("Invalid Entry, Kindly prooceed To your ride.")
else:
    print("Sorry you're not eligle for. the ride.")




# Task 5 -------------- Python Pizza Deliveries.


print('Welcome to python deliveries!')
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheeese? Y or N: ")

bill = 0

if size == 'S':
    bill = 15
    print("The small size pizza costs $15")
    if pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
        print(f"Your Final Bill is {bill}")
    else:
        print(f"Your Final Bill is {bill}")

elif size == 'M':
    bill = 20
    print("The medium size pizza costs $20")
    if pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
        print(f"Your Final Bill is {bill}")
    else:
        print(f"Your Final Bill is {bill}")

elif size == 'L':
    bill = 20
    print("The medium size pizza costs $20")
    if pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
        print(f"Your Final Bill is {bill}")
    else:
        print(f"Your Final Bill is {bill}")

else:
    print("Invalid Input, Kindly replace your order.")