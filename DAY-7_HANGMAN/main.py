import random

# CREATING THE HANGMAN GAME

# Step one --   i. randomly choose a word from a list, 
#               ii. ask the user to guess a letter in the word, 
#               iii. check if the guessed letter is one of the letters in the selected_word

# Step Two --   i. create a placeholder for the word using underscores.
#               ii. if guessed letter is in the word, replace uderscore with a word and display the output.
#               iii. if any false guess, maintain underscore.


word_list = ['apple', 'tame', 'ink', 'oven', 'cheese', 'final']

selected_word = random.choice(word_list)
# print(selected_word)

placeholder = "_" * len(selected_word)
print(placeholder)


guessed_letter = []
game_over = False

while not game_over:
    display = ''
    guess = input("Guess a letter from the word: ").lower()

    for letter in selected_word:
    
        if guess == letter:
            display += letter
            guessed_letter.append(letter)

        elif letter in guessed_letter:
            display += letter

        else:
            display += "_"
        
    print(display)

    if '_' not in display:
        print("You have won!!!")
        game_over = True


