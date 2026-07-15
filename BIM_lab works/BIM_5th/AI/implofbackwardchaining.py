# Backward Chaining
facts = {"A", "B"}
rules = {
    "C": ["A", "B"],
    "D": ["C"],
    "E": ["D"]
}
def prove(goal):
    if goal in facts:
        return True
    if goal not in rules:
        return False
    for item in rules[goal]:
        if not prove(item):
            return False
    return True
goal = "E"
if prove(goal):
    print("Goal", goal, "is proved.")
else:
    print("Goal", goal, "cannot be proved.")