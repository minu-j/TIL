#### 최적화 필요

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 델타검색으로 상하좌우 값 중에서 1만큼 큰 숫자를 가지는 칸 찾기
def move(start, n, x, y, step):
    for _ in range(4):
        if 0 <= x + dx[_] < N and 0 <= y + dy[_] < N and matrix[x + dx[_]][y + dy[_]] == n + 1:
            return move(start, matrix[x + dx[_]][y + dy[_]], x + dx[_], y + dy[_], step + 1)
    return start, step


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    moves = []

    # 2차원리스트를 순회하면서 각 항목별 이동횟수 찾기
    for i in range(N):
        for j in range(N):
            moves.append(move(matrix[i][j], matrix[i][j], i, j, 1))

    # 정답은 이동횟수가 가장 많은 값 중에서 가장 숫자가 작은 값
    ans = max(moves, key=lambda x: (x[1], -x[0]))

    print(f'#{tc + 1} {ans[0]} {ans[1]}')
