def select(depth):
    global cost
    global ans

    if depth == N and cost < ans:
        ans = cost
        return

    if cost >= ans:
        return

    for _ in range(N):
        if check[_] == 0:
            check[_] = 1
            cost += matrix[_][depth]
            select(depth + 1)
            check[_] = 0
            cost -= matrix[_][depth]


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    sel = [[0] * N for _ in range(N)]
    cost = 0
    ans = 999999999999999999999999999
    select(0)

    print(f'#{tc + 1} {ans}')
