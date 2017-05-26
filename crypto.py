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
    message = raw_input("Please enter the text you wish to encrypt:")
    
    # return the length of the original text
    length = len(message)
    start = 0
    c = 0


print cryptopy()
