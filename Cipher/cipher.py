"""
The Caesar Cipher

This Python script implements the Caesar cipher, an encryption that
shifts each letter of a plaintext input by a fixed number of
positions. This script will shift the plaintext by 15 positions.

It will turn each letter of the plaintext into an ASCII value and
shift that value by 15. If the value goes past the letter 'z', it
wraps around to the beginning of the alphabet.

Spaces and punctuation are not altered.
"""


def caesar_cipher(plaintext, shift=15):
    """
    This function takes a plaintext string and shifts each letter by
    15 positions in the alphabet. Non-letter characters remain
    unchanged.

    Parameters:
    plaintext (str): The input string to be encrypted.
    shift (int): The number of positions to shift each letter.

    Returns:
    str: The resulting ciphertext after applying the Caesar cipher.
    """
    ciphertext = ""

    for char in plaintext:

        # If the character is a letter, shift it by 15 positions
        if char.isalpha():
            # Determine the ASCII base for lowercase or
            # uppercase letters
            base = ord('a') if char.islower() else ord('A')
            # Shift character and wrap around the alphabet
            # using modulo operation
            shifted = (ord(char) - base + shift) % 26 + base
            ciphertext += chr(shifted)

        # Character is not a letter, leave it unchanged
        else:
            ciphertext += char

    return ciphertext


input_text = input("Please enter your plaintext: ")
encrypted_text = caesar_cipher(input_text)
print("Ciphertext:", encrypted_text)
