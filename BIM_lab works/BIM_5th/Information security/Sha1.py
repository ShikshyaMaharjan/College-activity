import hashlib

def generate_sha1(message):
    sha1 = hashlib.sha1()
    sha1.update(message.encode('utf-8'))
    return sha1.hexdigest()

while True:
    text = input("Enter text to hash: ")

    if text == "":
        print("Please enter some text.")
        continue

    print("SHA-1 Hash Value:", generate_sha1(text))
    break