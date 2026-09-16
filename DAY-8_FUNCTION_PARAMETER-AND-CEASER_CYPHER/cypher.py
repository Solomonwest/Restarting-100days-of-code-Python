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
        if i == ' ':
            pass
        else:
            index = alphabet.index(i)
            encrypted_data.append(encrypted_alphabet[index])

    # CONVERTING ENCRYPTED DATA INTO A STRING
    for letter in encrypted_data:
        encrypted_word += letter 
        
    print(f"your encrypted word is {encrypted_word}")
    print(f"your encrypted data is {encrypted_data}")

    
    
encrypt(original_text=text, shift_amount=shift)