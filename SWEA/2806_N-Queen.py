di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def position_queen(n, depth):
    if depth == n:
        return
    for _ in range(depth, n):
        


for tc in range(int(input())):
    N = int(input())
    matrix = [[0] * (N + 2) for _ in range(N + 2)]

    # 퀸이 들어갈 수 있는 위치 구하기

    # 체스판 테두리에 벽 치기
    for i in range(N + 2):
        if i == 0 or i == N + 1:
            for j in range(N + 2):
                matrix[i][j] = 2
        matrix[i][0] = 2
        matrix[i][N + 1] = 2

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(matrix[i][j])

    ans = 0

    print(f'#{tc + 1} {ans}')
