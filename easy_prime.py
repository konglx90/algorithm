print [x for x in range(3, 10000000, 2) if not [y for y in range(3, int(x ** 0.5) + 1, 2) if x % y == 0]]
