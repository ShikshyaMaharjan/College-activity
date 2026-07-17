facts = {
    "Fever": True,
    "Cough": True
}

rules = [
    (["Fever", "Cough"], "Flu"),
    (["Flu"], "Medicine"),
    (["Medicine"], "Recover")
]

fired = []

changed = True
while changed:
    changed = False
    for condition, result in rules:
        if all(facts.get(c, False) for c in condition) and result not in facts:
            facts[result] = True
            fired.append(result)
            changed = True

print("Initial Facts:")
print("Fever =", True)
print("Cough =", True)

print("\nRules Fired:")
for r in fired:
    print(r)

print("\nFinal Conclusion:")
for k in facts:
    print(k)