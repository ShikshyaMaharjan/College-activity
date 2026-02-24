# Rail Fence Cipher 
def encrypt(message, key):
    rails = ['' for _ in range(key)]
    row, step = 0, 1
    for char in message:
        rails[row] += char
        row += step
        if row == 0 or row == key - 1:
            step *= -1

    return ''.join(rails)
def decrypt(cipher, key):
    n = len(cipher)
    zigzag = []
    row, step = 0, 1
    for _ in range(n):
        zigzag.append(row)
        row += step
        if row == 0 or row == key - 1:
            step *= -1
    # Step 2: fill rails
    rails = ['' for _ in range(key)]
    index = 0
    for r in range(key):
        for i in range(n):
            if zigzag[i] == r:
                rails[r] += cipher[index]
                index += 1
    # Step 3: rebuild message
    result = ''
    counters = [0] * key
    for r in zigzag:
        result += rails[r][counters[r]]
        counters[r] += 1
    return result
message = input("Enter message: ")
key = int(input("Enter number of rails: "))
cipher = encrypt(message, key)
print("Encrypted:", cipher)
plain = decrypt(cipher, key)
print("Decrypted:", plain)