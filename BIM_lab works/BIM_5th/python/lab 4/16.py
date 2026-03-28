def make_multiplier(n):
    def multiplier(*args):
        if len(args) == 1:
            return args[0] * n
        return [x * n for x in args]
    return multiplier



times3 = make_multiplier(3)
print(times3(5))       
print(times3(1, 2, 3))  