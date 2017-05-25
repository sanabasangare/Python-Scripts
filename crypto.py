"""
Cryptopy:
This program is used to encrypt words and present 
the encoded message. It can also decrypt a ciphertext
into plain text
"""

def cryptopy():
  	# hint: reply with "encrypt" or "decrypt"
    reply = raw_input("Do you want to encrypt or decrypt.\
 (please type <<encrypt>> or <<decrypt>>")
    
    # If the answer is "encrypt", encode the message.
    if reply == "encrypt":
        return encrypt()
    # Otherwise, decode the message.
    elif reply == "decrypt":
        return decrypt()

print cryptopy()