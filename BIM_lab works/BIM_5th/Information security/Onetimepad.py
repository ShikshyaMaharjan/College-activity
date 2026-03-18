def otp_encrypt(text,key):
    result=""

    for i in range (len(text)):
        p= ord(text[i])-65
        k= ord(key[i])-65
        c= (p+k) %26
        result +=chr(c+65)
    return result
def otp_decrypt(cipher,key):
    result= ""
    for i in range (len(cipher)):
        c= ord(cipher[i])-65
        k= ord(key[i])-65
        p= (c-k) %26
        result +=chr(p+65)
    return result 
text= input("Enter plaintext (A-Z only):").upper()
key= input("Enter key(same length):").upper()

if len(text) != len(key):
    print("Error: key length must be same as text")
else:
    cipher= otp_encrypt(text, key)
    print("Cipher text:",cipher)

    plain =otp_decrypt(cipher,key)
    print("Decrypted text:",plain)
