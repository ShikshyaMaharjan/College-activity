from sklearn.naive_bayes import GaussianNB

# Dataset: [Weather, Temperature]
# 1 = Good conditions, 0 = Bad conditions
X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [0, 0]
]

# Labels: 1 = Play, 0 = Don't Play
y = [1, 1, 0, 0, 1, 0]

# Create model
model = GaussianNB()

# Train model
model.fit(X, y)

# Test data (Sunny + Hot condition)
test = [[1, 1]]

# Prediction
result = model.predict(test)

if result[0] == 1:
    print("Play")
else:
    print("Don't Play")