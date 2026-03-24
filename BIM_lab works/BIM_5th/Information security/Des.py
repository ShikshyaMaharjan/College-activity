from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# Generate 8-byte key
secret_key = get_random_bytes(8)

# Function to add padding
def add_padding(msg):
    pad_len = 8 - (len(msg) % 8)
    return msg + (chr(pad_len) * pad_len)

# Function to remove padding
def remove_padding(msg):
    pad_len = ord(msg[-1])
    return msg[:-pad_len]

# Take user input
plain_text = input("Enter your message: ")

# Prepare message
padded_text = add_padding(plain_text)

# Create cipher object
des_cipher = DES.new(secret_key, DES.MODE_ECB)

# Encrypt
encrypted_bytes = des_cipher.encrypt(padded_text.encode())
encrypted_text = base64.b64encode(encrypted_bytes).decode()

print("Encrypted Text:", encrypted_text)

# Decrypt
des_decipher = DES.new(secret_key, DES.MODE_ECB)
decrypted_bytes = des_decipher.decrypt(encrypted_bytes)
final_text = remove_padding(decrypted_bytes.decode())

print("Decrypted Text:", final_text)