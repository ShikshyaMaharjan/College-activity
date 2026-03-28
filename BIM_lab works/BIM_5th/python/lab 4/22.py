def sum_to_n(n):
    if n == 1: # base case
        return 1
    else:
        return n + sum_to_n(n - 1) # recursive call
print(sum_to_n(5))