numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]
print("Squares:", squares)

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)