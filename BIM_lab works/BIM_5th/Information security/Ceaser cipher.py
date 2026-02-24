def encrypt(text,s):
    result=""
    for char in text:
        if char.isupper():
            result += chr((ord(char)+s-65)% 26+65)
        elif char.islower():
            result += chr((ord(char)+ s- 97)% 26 + 97)
        else:
            result += char
    return result

text = input("Enter the text:")
s = int(input("Enter the shift value:"))

print("Text  :",text)
print("Shift  :",s)
print("Chipher :",encrypt(text,s))

def decrypt(text,s):
    result =""
    for char in text:
        if char.isupper():
            result += chr((ord(char)-s-65)% 26+65)
        elif char.islower():
            result += chr((ord(char)- s- 97)% 26 + 97)
        else:
            result += char
    return result

cipher = input("Enter the Chiper text:")
s = int(input("Enter the shift value:"))

print("Chiper  :",cipher)
print("Shift  :",s)
print("Text :",decrypt(cipher,s))