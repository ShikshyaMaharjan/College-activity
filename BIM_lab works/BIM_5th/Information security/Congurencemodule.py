# Modular Congruence Program

# Function to check if a ≡ b (mod m)
def check_congruence(a, b, m):
    if (a - b) % m == 0:
        return True
    else:
        return False

# Function to solve a * x ≡ b (mod m)
def solve_congruence(a, b, m):
    for x in range(m):
        if (a * x) % m == b % m:
            return x
    return None

# Input values
# Input values
a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

# Check congruence
if (a - b) % m == 0:
    print(f"{a} is congruent to {b} modulo {m} is congurent")
else:
    print(f"{a} is NOT congruent to {b} modulo {m} is not congurent")

# Solve for x in a*x ≡ b (mod m)
x = solve_congruence(a, b, m)
if x is not None:
    print(f"A solution for a*x ≡ b (mod {m}) is x = {x}")
else:
    print(f"No solution exists for a*x ≡ b (mod {m})")