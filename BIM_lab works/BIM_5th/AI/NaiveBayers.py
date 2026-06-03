P_yes = 0.71
P_no = 0.29

P_sunny_given_yes = 3/10
P_sunny_given_no = 2/4

P_sunny = 0.35

# Bayes theorem
P_yes_sunny = (P_sunny_given_yes * P_yes) / P_sunny
P_no_sunny = (P_sunny_given_no * P_no) / P_sunny

print("P(Yes|Sunny) =", round(P_yes_sunny,2))
print("P(No|Sunny) =", round(P_no_sunny,2))

if P_yes_sunny > P_no_sunny:
    print("Player should Play")
else:
    print("Player should Not Play")