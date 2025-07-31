#!/usr/bin/env python
# coding: utf-8

# In[3]:
def caesar_cipher(text, shift, mode):
   result = []
   
   if mode == 'decrypt':
       shift = -shift
       
   for char in text:
       if char.isalpha():
           start = ord('A') if char.isupper() else ord('a')
           offset = (ord(char) - start + shift) % 26
           result.append(chr(start + offset))
       else:
           result.append(char)
   
   return ''.join(result)

def main():
   while True:
       print("\nCaesar Cipher Menu:")
       print("1. Encrypt")
       print("2. Decrypt")
       print("3. Exit")
       
       choice = input("Enter your choice (1/2/3):")
       
       if choice == '1':
           plaintext = input("Enter the plaintext to encrypt: ")
           shift = int(input("Enter the shift value (integer): "))
           ciphertext = caesar_cipher(plaintext, shift, 'encrypt')
           print("Encrypted text:", ciphertext)
           
       elif choice == '2':
           ciphertext = input("Enter the ciphertext to decrypt: ")
           shift = int(input("Enter the shift value (integer): "))
           decrypted_text = caesar_cipher(ciphertext, shift, 'decrypt')
           print("Decrypted text:", decrypted_text)
           
       elif choice == '3':
           print("Exiting...")
           break
       
       else:
           print("Invalid choice. Please enter 1, 2, or 3.")
       
if __name__ == "__main__":
   main()




# In[3]:


def rail_fence_encrypt(text, key):
    fence = [''] * key

    # Place each character in the correct "rail"
    row = 0
    step = 1
    for char in text:
        fence[row] += char
        row += step
        if row == 0 or row == key - 1:
            step = -step

    # Join all rows to get the encrypted text
    return ''.join(fence)

# User input
text = input("Enter the text to encrypt: ")
key = int(input("Enter the key (number of rails): "))

# Encryption
encrypted_text = rail_fence_encrypt(text, key)
print("Encrypted text:", encrypted_text)


# In[2]:


def transposition(text, key):
    cols = ['' for _ in key]
    for i, char in enumerate(text.ljust(len(key) * ((len(text) + len(key) - 1) // len(key)))):
        cols[i % len(key)] += char
    return ''.join(cols[i] for i in sorted(range(len(key)), key=lambda k: key[k]))

text = input("Enter text: ")
key = input("Enter key: ")
encrypted_text = transposition(text, key)
print("Encrypted text:", encrypted_text)


# In[1]:


def transposition(text, key):
    cols = ['' for _ in key]
    for i, char in enumerate(text.ljust(len(key) * ((len(text) + len(key) - 1) // len(key)))):
        cols[i % len(key)] += char
    return ''.join(cols[i] for i in sorted(range(len(key)), key=lambda k: key[k]))

text = input("Enter text: ") 
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")
encrypted_text = transposition(transposition(text, key1), key2)
print("Encrypted text:", encrypted_text)


# In[ ]:




