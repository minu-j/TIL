def comb(n, m):   # 조합
    def fact(x):   # 팩토리얼
        if x == 1 or x == 0:
            return 1
        else:
            f = x * fact(x - 1)
        return f
    c = fact(n) // (fact(n - m) * fact(m))
    return c

