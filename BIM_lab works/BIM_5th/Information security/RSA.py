# Basic RSA Algorithm (Modified Version)

# Function to find GCD
def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Function to find modular inverse
def find_inverse(e, phi):
    i = 1
    while i < phi:
        if (e * i) % phi == 1:
            return i
        i += 1

# Step 1: Select two prime numbers
prime1 = 5
prime2 = 7

# Step 2: Calculate n and phi(n)
n = prime1 * prime2
phi_n = (prime1 - 1) * (prime2 - 1)

# Step 3: Choose e such that gcd(e, phi) = 1
e = 2
while find_gcd(e, phi_n) != 1:
    e += 1

# Step 4: Calculate d (private key)
d = find_inverse(e, phi_n)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Take message input
message = int(input("Enter a number less than n: "))

# Encryption process
encrypted_msg = pow(message, e, n)
print("Encrypted value:", encrypted_msg)

# Decryption process
decrypted_msg = pow(encrypted_msg, d, n)
print("Decrypted value:", decrypted_msg)