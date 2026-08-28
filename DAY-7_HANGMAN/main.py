import random

# CREATING THE HANGMAN GAME

# Step one --   i. randomly choose a word from a list, 
#               ii. ask the user to guess a letter in the word, 
#               iii. check if the guessed letter is one of the letters in the selected_word

# Step Two --   i. create a placeholder for the word using underscores.
#               ii. if guessed letter is in the word, replace uderscore with a word and display the output.
#               iii. if any false guess, maintain underscore.

# Step Three -- i. create a while loop, to permit repetitive guessing 
#               ii. store the correct guess in a string and represent unguessed letters with an underscore
#               iii. create a variable called live and equal to 6, for every wrong guess reduce live by 1.

# Step Four --  i. introduce the hangman ASCII art for different lives in a list.
#               ii. For each invalid guess display the appropriate hangman status
#               iii. Once the lives are exhausted print game over
                

word_list = ['apple', 'tame', 'ink', 'oven', 'cheese', 'final']

selected_word = random.choice(word_list)

print(r'''
 
      
  _  _   _   _  _  ___ __  __   _   _  _ 
 | || | /_\ | \| |/ __|  \/  | /_\ | \| |
 | __ |/ _ \| .` | (_ | |\/| |/ _ \| .` |
 |_||_/_/ \_\_|\_|\___|_|  |_/_/ \_\_|\_|

          
''')


placeholder = "_" * len(selected_word)
print(placeholder)


guessed_letter = []
game_over = False

life = 6

stages = [ r'''
          
      +---------+
      |         |
      0         |
     /|\        |
     / \        |
                |
    =============
''', r'''
      +---------+
      |         |
      0         |
     /|\        |
     /          |
                |
    =============
''', r'''
      +---------+
      |         |
      0         |
     /|\        |
                |
                |
    =============
''', r'''
      +---------+
      |         |
      0         |
     /|         |
                |
                |
    =============
''', '''
      +---------+
      |         |
      0         |
      |         |
                |
                |
    =============
''', '''
      +---------+
      |         |
      0         |
                |
                |
                |
    =============
''', '''
      +---------+
      |         |
                |
                |
                |
                |
    =============
'''
]

while not game_over:
    display = ''
    guess = input("Guess a letter from the word: ").lower()

    if guess in guessed_letter:
        print(f'You already guessed letter {guess}')

    for letter in selected_word:
    
        if guess == letter:
            display += letter
            guessed_letter.append(letter)

        elif letter in guessed_letter:
            display += letter

        else:
            display += "_"
        
    print(display)

#           ASCII art display
    if guess in selected_word:
        print(stages[life])

    else:
        life -=1
        print(stages[life])
        print(f"wrong guess!! you have {life} lifeline left")

#           Game over condition
    if '_' not in display:
        print("You have won!!!")
        game_over = True

    elif life == 0:
        print(f"Game over, You lost! The word is {selected_word}")
        game_over = True




