def perm(n, m):
    arr = [1] * n
    sel = [0] * m
    check = [0] * n
    ans = 0

    def f(depth):
        nonlocal ans
        if depth == 2:
            ans += 1
            return

        for i in range(len(arr)):
            if not check[i]:
                sel[depth] = arr[i]
                check[i] = 1
                f(depth + 1)
                check[i] = 0
    f(0)
    return ans


print(perm(4, 2))
