# Forward Chaining

facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]

for precondition, conclusion in rules:
    if precondition.issubset(facts):
        facts.add(conclusion)

print("Derived Facts:")
print(sorted(facts))