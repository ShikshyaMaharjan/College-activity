data = [
    ("Sunny","No","Yes"),
    ("Sunny","Yes","No"),
    ("Rainy","No","Yes"),
    ("Rainy","Yes","No"),
    ("Overcast","No","Yes"),
    ("Sunny","No","Yes")
]

test_weather = "Sunny"
test_windy = "No"

classes = ["Yes","No"]

for c in classes:
    subset = [x for x in data if x[2]==c]

    prior = len(subset)/len(data)

    weather = sum(1 for x in subset if x[0]==test_weather)/len(subset)

    windy = sum(1 for x in subset if x[1]==test_windy)/len(subset)

    prob = prior*weather*windy

    print(c,"Probability =",prob)