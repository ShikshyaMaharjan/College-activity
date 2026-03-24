from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Function to add padding (PKCS-style)
def add_pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + chr(pad_len) * pad_len

# Function to remove padding
def remove_pad(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]

# Generate secret key (16 bytes for AES-128)
# Fixed 16-byte key (AES-128)
secret_key = b'1234567890123456'

# Take input
plain_text = input("Enter your text: ")

# Apply padding
padded_text = add_pad(plain_text)

# Create AES object
aes_cipher = AES.new(secret_key, AES.MODE_ECB)

# Encrypt
encrypted_bytes = aes_cipher.encrypt(padded_text.encode())
encoded_text = base64.b64encode(encrypted_bytes).decode()

print("Encrypted Text:", encoded_text)

# Decrypt
aes_decipher = AES.new(secret_key, AES.MODE_ECB)
decrypted_bytes = aes_decipher.decrypt(encrypted_bytes)
final_text = remove_pad(decrypted_bytes.decode())

print("Decrypted Text:", final_text)