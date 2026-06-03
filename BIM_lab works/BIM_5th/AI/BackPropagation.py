# Simple Backpropagation Example

# Input and target
x = 1
target = 1

# Initial weight
w = 0.5

# Learning rate
lr = 0.9

# Training for 5 iterations
for i in range(5):
    # Forward pass
    output = x * w

    # Error
    error = target - output

    # Backpropagation (weight update)
    w = w + (lr * error * x)

    print("Iteration:", i+1)
    print("Output:", output)
    print("Error:", error)
    print("Updated Weight:", w)
    print()