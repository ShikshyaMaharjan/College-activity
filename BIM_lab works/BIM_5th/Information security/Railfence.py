# Rail Fence Cipher Correct Version

def encrypt(message, key):

    rails = ['' for _ in range(key)]

    row = 0
    step = 1

    for char in message:

        rails[row] += char

        # change direction BEFORE updating row
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    return ''.join(rails)


def decrypt(cipher, key):

    n = len(cipher)

    zigzag = []

    row = 0
    step = 1

    for i in range(n):

        zigzag.append(row)

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step


    rails = ['' for _ in range(key)]

    index = 0

    for r in range(key):
        for i in range(n):
            if zigzag[i] == r:
                rails[r] += cipher[index]
                index += 1


    result = ''

    counters = [0] * key

    for r in zigzag:

        result += rails[r][counters[r]]

        counters[r] += 1


    return result


# Main

message = input("Enter message: ")
key = int(input("Enter key: "))

cipher = encrypt(message, key)

print("Encrypted:", cipher)

plain = decrypt(cipher, key)

print("Decrypted:", plain)