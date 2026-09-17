
print(r"""

__        _______ _     ____ ___  __  __ _____ 
\ \      / / ____| |   / ___/ _ \|  \/  | ____|
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
  \ V  V / | |___| |__| |__| |_| | |  | | |___ 
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|

 _____ ___     ____    _    _____ ____    _    ____     ____ ___ ____  _   _ _____ ____  
|_   _/ _ \   / ___|  / \  | ____/ ___|  / \  |  _ \   / ___|_ _|  _ \| | | | ____|  _ \ 
  | || | | | | |     / _ \ |  _| \___ \ / _ \ | |_) | | |    | || |_) | |_| |  _| | |_) |
  | || |_| | | |___ / ___ \|  |__ ___) / ___ \|  _ <  | |___ | ||  __/|  _  | |___|  _ < 
  |_| \___/   \____/_/   \_\_____|____/_/   \_\_| \_\  \____|___|_|   |_| |_|_____|_| \_\
      


""")


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

text = input("Type your message: \n").lower()

shift = int(input("Type the shift number: \n"))

encrypted_alphabet = []

encrypted_data = []

def encrypt(original_text, shift_amount):

    encrypted_word = ''
    start = len(alphabet) - (shift_amount-1)

    #  CREATE AN ENCRYPTED ALPHABET LIST BASED ON SHIFT AMOUNT
    for i in range(1, shift_amount):
        encrypted_alphabet.append(alphabet[start])
        start +=1

    for i in range(0, ((start + 1) - shift_amount)):
        encrypted_alphabet.append(alphabet[i])

    # ENCODE BY TAKING THE INDEX OF EVERY LETTER FROM THE ALPHABET LIST AND USE SAME INDEX TO FETCH FROM ENCRYPTED ALPHABET
    for i in original_text:
        if i not in alphabet:
            encrypted_data.append(i)
        else:
            index = alphabet.index(i)
            encrypted_data.append(encrypted_alphabet[index])

    # CONVERTING ENCRYPTED DATA INTO A STRING
    for letter in encrypted_data:
        encrypted_word += letter 

    print(f"your encrypted word is: {encrypted_word}")
    


decrypted_data = []
def decrypt(original_text, shift_amount):


    decrypted_word = ''
    start = len(alphabet) - (shift_amount-1)

    #  CREATE AN ENCRYPTED ALPHABET LIST BASED ON SHIFT AMOUNT
    for i in range(1, shift_amount):
        encrypted_alphabet.append(alphabet[start])
        start +=1

    for i in range(0, ((start + 1) - shift_amount)):
        encrypted_alphabet.append(alphabet[i])

    # DECODE BY TAKING THE INDEX OF EVERY LETTER FROM THE ENCYPTED ALPHABET LIST AND USE SAME INDEX TO FETCH FROM ALPHABET LIST
    for i in original_text:
        if i not in encrypted_alphabet:
            decrypted_data.append(i)
        else:
            index = encrypted_alphabet.index(i)
            decrypted_data.append(alphabet[index])

    # CONVERTING ENCRYPTED DATA INTO A STRING
    for letter in decrypted_data:
        decrypted_word += letter 

    print(f"your decrypted word is: {decrypted_word}")





if direction == 'encode':
    encrypt(original_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid Command, Try Again")