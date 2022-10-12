from collections import deque
from pprint import pprint


# 해당 좌표의 벽돌을 깨트리기
def break_brick(matrix, y, x, break_range):
    matrix[y][x] = 0

    for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
        for count in range(1, break_range):
            if 0 <= y + di * count < H and 0 <= x + dj * count < W:
                break_brick(matrix, y + di * count, x + dj * count, matrix[y + di * count][x + dj * count])


# 가장 위 벽돌을 찾아서 깨트리기
def shoot(matrix, column):

    target = 0
    for row in range(H):
        if matrix[row][column]:
            target = row
            break

    break_brick(matrix, target, column, matrix[target][column])
    fall(matrix)

    return matrix


def games(matrix, depth):
    global ans

    if depth >= N:
        count = 0
        for i in range(H):
            for j in range(W):
                if matrix[i][j]:
                    count += 1
        if count < ans:
            ans = count
        return

    for point in range(W):

        matrix_copy = []  # 딥카피
        for _ in range(H):
            matrix_copy.append(matrix[_][:])

        shoot(matrix_copy, point)

        games(matrix_copy, depth + 1)


def fall(matrix):
    for c in range(W):
        col_stack = []
        for r in range(H):
            if matrix[r][c]:
                col_stack.append(matrix[r][c])
                matrix[r][c] = 0
        for rr in range(H - 1, -1, -1):
            if col_stack:
                matrix[rr][c] = col_stack.pop()
    return matrix


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    matrix_original = [list(map(int, input().split())) for _ in range(H)]
    ans = 999999999999999999999999999

    games(matrix_original, 0)

    print(f'#{tc + 1} {ans}')
