def rsp(n, ni, m, mi):
    if ni == mi:
        return min(n, m)
    elif ni == 1:
        if mi == 2:
            return m
        elif mi == 3:
            return n
    elif ni == 2:
        if mi == 1:
            return n
        elif mi == 3:
            return m
    elif ni == 3:
        if mi == 1:
            return m
        elif mi == 2:
            return n


def battle(depth, i, j):
    if i[1] == j[1]:
        print(i)
        stack[depth].append(i)
        return
    battle(depth + 1, i, (i[1] + j[1]) // 2)
    battle(depth + 1, (i[1] + j[1]) // 2 + 1, j)


for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        arr[i] = (i + 1, arr[i])
    stack = [[] for i in range((N + 1) // 2)]

    ans = 0

    battle(0, arr[0], arr[N - 1])

    print(f'#{tc + 1} {ans}')