def caesar_cipher_encrypt(txt, shft):
    encrypted_text = ""
    for char in txt:
        if char.isalpha():
            shifted = ord(char) + shft
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(txt, shft):
    return caesar_cipher_encrypt(txt, -shft)

def main():
    while True:
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\n")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shft = int(input("Enter the shft value: "))
            encrypted_message = caesar_cipher_encrypt(message, shft)
            print("Encrypted message:", encrypted_message)
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shft = int(input("Enter the shft value: "))
            decrypted_message = caesar_cipher_decrypt(message, shft)
            print("Decrypted message:", decrypted_message)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
