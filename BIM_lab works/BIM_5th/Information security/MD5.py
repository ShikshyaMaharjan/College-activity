import hashlib

# Function to compute MD5 hash
def md5_hash(message):
    # Create MD5 object
    md = hashlib.md5()
    
    # Convert string to bytes and update hash
    md.update(message.encode('utf-8'))
    
    # Return final hexadecimal hash
    return md.hexdigest()


# Main program
text = input("Enter message: ")

result = md5_hash(text)

print("MD5 Hash Value:", result)