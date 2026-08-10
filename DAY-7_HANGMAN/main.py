import random

# CREATING A HANGMAN GAME

# Step one --   i. randomly choose a word from a list, 
#               ii. ask the user to guess a letter in the word, 
#               iii. check if the guessed letter is one of the letters in the selected_word, print right if it's and wrong if not.

# Step Two -- 


word_list = ['apple', 'tame', 'ink', 'oven', 'cheese', 'final']

selected_word = word_list[random.randint(0, 5)]
print(selected_word)

placeholder = ''
for letter in selected_word:
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter from the word: ").lower()

display = ''
for letter in selected_word:
    
    if guess == letter:
        display += letter
    else:
        display += "_"
    
print(display)