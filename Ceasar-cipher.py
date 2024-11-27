import string

def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the input text using Caesar Cipher with the given shift.
    """
    result = []
    for char in text:
        if char.isalpha():  # Check if character is alphabetic
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)  # Keep non-alphabetic characters unchanged
    return ''.join(result)

def caesar_cipher_decrypt(text, shift):
    """
    Decrypts the input text using Caesar Cipher with the given shift.
    """
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Program!")
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("3. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                text = input("Enter the message to encrypt: ")
                shift = int(input("Enter the shift value (1-25): "))
                encrypted = caesar_cipher_encrypt(text, shift)
                print(f"Encrypted Message: {encrypted}")
            elif choice == 2:
                text = input("Enter the message to decrypt: ")
                shift = int(input("Enter the shift value (1-25): "))
                decrypted = caesar_cipher_decrypt(text, shift)
                print(f"Decrypted Message: {decrypted}")
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
