letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text, shift):
    ciphertext = ''
    for letter in text:
        lower_letter = letter.lower()
        index = letters.find(lower_letter)
        if index == -1:
            ciphertext += letter
        else:
            nindex = (index + shift) % 26
            ciphertext += letters[nindex]  # add .upper() if original letter was uppercase
    return ciphertext

def decrypt(text, shift):
    plaintext = ''
    for letter in text:
        lower_letter = letter.lower()
        index = letters.find(lower_letter)
        if index == -1:
            plaintext += letter
        else:
            nindex = (index - shift) % 26
            plaintext += letters[nindex]
    return plaintext

print("-------Encryptor/Decryptor-------\n")
print("Choose an option:\n1. Encrypt\n2. Decrypt\n")
option = input("Enter your choice (1 or 2): ")

if option == '1':
    print("\nYou chose to Encrypt the text.\n")
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    ciphertext = encrypt(text, shift)
    print("\nCipher text:", ciphertext)

elif option == '2':
    print("\nYou chose to Decrypt the text.\n")
    text = input("Enter the Cipher text to decrypt: ")
    shift = int(input("Enter the shift value: "))
    plaintext = decrypt(text, shift)
    print("\nPlain text:", plaintext)

else:
    print("Invalid choice. Please enter 1 or 2.")
