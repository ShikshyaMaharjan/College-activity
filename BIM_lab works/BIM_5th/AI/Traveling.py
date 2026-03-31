from itertools import permutations

def travelling_salesman_problem(graph, start_city):
    # Get total number of cities
    num_cities = len(graph)

    # Create list of all cities except starting city
    cities = []
    for city in range(num_cities):
        if city != start_city:
            cities.append(city)

    # Set minimum cost as infinity
    min_cost = float('inf')
    best_route = []

    # Generate all possible routes
    possible_routes = permutations(cities)

    # Check every possible route
    for route in possible_routes:
        current_cost = 0
        current_city = start_city

        # Calculate cost of current route
        for next_city in route:
            current_cost += graph[current_city][next_city]
            current_city = next_city

        # Add cost to return to starting city
        current_cost += graph[current_city][start_city]

        # Update minimum cost and best route
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = [start_city] + list(route) + [start_city]

    return min_cost, best_route


# Distance matrix (graph)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Starting city
start_city = 0

# Function call
minimum_cost, route = travelling_salesman_problem(graph, start_city)

# Print output
print("Minimum Cost:", minimum_cost)
print("Best Route:", route)