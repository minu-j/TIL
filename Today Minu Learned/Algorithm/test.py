def comb(n, m):
    def fact(x):
        if x == 1 or x == 0:
            return 1
        else:
            f = x * fact(x - 1)
        return f
    c = fact(n) / (fact(n - m) * fact(m))
    return c


while True:
    print(comb(int(input()), int(input())))