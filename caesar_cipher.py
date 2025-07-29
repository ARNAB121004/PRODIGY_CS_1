def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char  # Non-alphabet characters stay the same
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryeption/Decryption ===")
    choice = input("Do you want to Encrypt or Decrypt?: ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please choose E or D.")
        return
    
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'E':
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted Message:", result)
    else:
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted Message:", result)

if __name__ == "__main__":
    main()
