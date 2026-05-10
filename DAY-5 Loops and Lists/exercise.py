import random

# FizzBuzz Exercise

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# 1. Your program should print each number from 1 to 100 in turn and include number 100.

# 2. But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

# 3. When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# 4. And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 5 == 0:
        num = "Buzz"
    elif num % 3 == 0:
        num = "Fizz"
    print(num)




# Password Generator


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Python Password Generator!")

nr_letters = int(input("How many letters do you want in your password? "))
nr_numbers = int(input("How many numbers do you want in your password? "))
nr_symbols = int(input("How many symbols do you want in your password? "))


#                   MY SOLUTION
lett = []
random.shuffle(letters)

for i in letters:
    if len(lett) < nr_letters:
        lett.append(i)
        # print(lett)

numm = []
random.shuffle(numbers)

for i in numbers:
    if len(numm) < nr_numbers:
        numm.append(i)

symb = []
random.shuffle(symbols)

for i in symbols:
    if len(symb) < nr_symbols:
        symb.append(i)



password = lett + numm + symb
random.shuffle(password)

str_password = ''
for p in password:
    str_password += p
print(f"Your Password is {str_password}")


#            ANGELA'S SIMPLE SOLUTION 

secret_key = ""

for x in range(0, nr_letters):
    secret_key += random.choice(letters)

for x in range(0, nr_numbers):
    secret_key += random.choice(numbers)

for x in range(0, nr_symbols):
    secret_key += random.choice(symbols)


print(f"Your New Password is {secret_key}")


#           ANGELA'S HARD SOLUTION

secret_key = []

for x in range(0, nr_letters):
    secret_key += random.choice(letters)

for x in range(0, nr_numbers):
    secret_key += random.choice(numbers)

for x in range(0, nr_symbols):
    secret_key += random.choice(symbols)

secret_pass = ""
for i in secret_key:
    secret_pass += random.choice(secret_key)
    
print(f"Your Hard Password is {secret_pass}")