# Simple Perceptron Program

w1 = 0
w2 = 0
b = 0
lr = 0.1

x = [[0,0], [0,1], [1,0], [1,1]]
t = [0,0,0,1]

for i in range(4):
    y = x[i][0]*w1 + x[i][1]*w2 + b

    if y >= 0:
        out = 1
    else:
        out = 0

    error = t[i] - out

    w1 = w1 + lr * error * x[i][0]
    w2 = w2 + lr * error * x[i][1]
    b = b + lr * error

print("Weight1 =", w1)
print("Weight2 =", w2)
print("Bias =", b)