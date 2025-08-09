# Caesar Cipher - Text Encryption and Decryption

This is a simple Python program that implements the **Caesar Cipher** algorithm. It allows users to **encrypt** or **decrypt** text messages using a shift value.

## What is Caesar Cipher?

The Caesar Cipher is one of the oldest known encryption techniques. Each letter in the message is shifted by a fixed number of positions in the alphabet. For example, with a shift of `3`, `A` becomes `D`, `B` becomes `E`, and so on.


## How It Works

- The user is asked whether they want to encrypt or decrypt.
- Then, the user enters the message.
- Finally, a shift value (an integer) is entered to perform the transformation.
- If the shift values are different for encryption and decryption, then the original message cannot be decrypted properly. Hence, the shift values for both encryption and decryption should be the same.

## Example

Encrypt or Decrypt (E/D): E

Enter your message: Hello World

Enter shift value (e.g., 3): 3

Encrypted message: Khoor Zruog





Encrypt or Decrypt (E/D): D

Enter your message: Khoor Zruog

Enter shift value (e.g., 3): 3

Decrypted message: Hello World

## Requirements

- Python 3.x

## Features

- Supports both encryption and decryption

- Handles both uppercase and lowercase letters

- Ignores and preserves non-alphabetic characters like spaces and punctuation
