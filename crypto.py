"""
Cryptopy:
This program is used to encrypt words and present
the encoded message. It can also decrypt a ciphertext
into plain text
"""


def cryptopy():
    # hint: reply with "encrypt" or "decrypt"
    reply = raw_input("Would you like to encrypt or decrypt\
 (please type 'encrypt' or 'decrypt'): ")

    # If the answer is "encrypt", encode the message.
    if reply == "encrypt":
        return encryption()
    # Otherwise, decode the message.
    elif reply == "decrypt":
        return decryption()


# The encryption function
def encryption():
    message = raw_input("Please enter the text you wish to encrypt: ")
    
    # return the length of the original text
    length = len(message)
    start = 0
    c = 0

    # Producing the encrypted message
    while start < length:
        char = message[start]
        conversion1 = start
        start = conversion1 + 1

        # Assigning a value
        if c < 1:
            encoded_message = ""

        conversion2 = c + 1
        c = conversion2
        index = ord(char)
        alg = index - 8
        encoded_char = chr(alg)
        conversion4 = encoded_message + encoded_char
        encoded_message = conversion4

    print encoded_message

    raw_input("Press enter to exit")


# Decryption function
def decryption():
    message = raw_input("Please enter the ciphertext you wish to decrypt: ")
    
    # return the length of the original text
    length = len(message)
    start = 0
    c = 0


cryptopy()
