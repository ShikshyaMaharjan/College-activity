# Simple Genetic Algorithm

population = [5, 8, 12, 3]

# Fitness Function
def fitness(x):
    return x * x

print("Initial Population:", population)

# Find Best Individual
best = population[0]

for i in population:
    if fitness(i) > fitness(best):
        best = i

print("Best Solution:", best)
print("Fitness Value:", fitness(best))