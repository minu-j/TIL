from collections import deque
from pprint import pprint


# 가장 위 벽돌 찾기
def find_top(c):
    top = 0
    for cr in range(H):
        if matrix[cr][c]:
            top = cr
            break
    return top


# 해당 칸의 벽돌 깨기
def break_brick(y1, x1):

    def break_brick_queue(y, x):
        n = matrix[y][x] - 1
        matrix[y][x] = 0

        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            dy, dx = y, x
            for _ in range(n):
                if 0 <= dy + di < H and 0 <= dx + dj < W:
                    if matrix[dy + di][dx + dj]:
                        brick_queue.append((dy + di, dx + dj))
                dy += di
                dx += dj

    brick_queue = deque()
    brick_queue.append((y1, x1))

    while brick_queue:
        now = brick_queue.popleft()
        break_brick_queue(*now)


# 빈 블럭 메꾸기
def fall(mrx):
    for mj in range(W):
        bricks = []
        for mi in range(H):
            if mrx[mi][mj]:
                bricks.append(mrx[mi][mj])
                mrx[mi][mj] = 0
        print(bricks)
        for idx in zip(range(H - 1, H - len(bricks) - 1, -1), range(len(bricks) - 1, -1, -1)):
            print(idx)
            mrx[idx[0]][mj] = bricks[idx[1]]
    pprint(mrx)


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    matrix_original = [list(map(int, input().split())) for _ in range(H)]

    for column in range(W):
        matrix = [[] for _ in range(H)]
        for _ in range(H):
            matrix[_] = matrix_original[_][:]
        break_brick(find_top(column), column)

        pprint(matrix)
        fall(matrix)

    ans = 0

    print(f'#{tc + 1} {ans}')
