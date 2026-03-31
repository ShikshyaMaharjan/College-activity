
import hashlib
def sha256_hash(message):
    sha = hashlib.sha256()
    data = message.encode('utf-8')
    sha.update(data)
    return sha.hexdigest()
print("===== SHA-2 (SHA-256) Hash Generator =====")
text = input("Enter message: ")
result = sha256_hash(text)
print("Original Message:", text)
print("SHA-256 Hash Value:", result)