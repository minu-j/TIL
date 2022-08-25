def position_queen(n, depth):
    if depth == n:
        queens.append(sel[::])
        return
    for _ in range(n):
        if not check[_]:
            sel[depth] = (depth, _)
            check[_] = 1
            position_queen(n, depth + 1)
            check[_] = 0
            sel[depth] = 0


for tc in range(int(input())):
    N = int(input())

    sel = [0] * N
    check = [0] * N
    queens = []

    position_queen(N, 0)

    di = [1, 1]
    dj = [1, -1]

    ans = 0

    # 대각선 방향을 확인해야 합니다
    for i in queens:


    print(f'#{tc + 1} {ans}')
