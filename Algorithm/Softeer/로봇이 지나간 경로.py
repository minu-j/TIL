import sys

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

# 시작점 찾기
def find_start(i, j):
    global si, sj, direction
    count = 0
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < H and 0 <= nj < W and matrix[ni][nj] == '#' and (ni, nj) not in visited:
            visited.add((ni, nj))
            find_start(ni, nj)
            count += 1
    if not count:
        si, sj = i, j
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < H and 0 <= nj < W and matrix[ni][nj] == '#':
                direction = d
        return

# 경로찾기
def find_route(i, j, direction, s):
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < H and 0 <= nj < W and matrix[ni][nj] == '#' and (ni, nj) not in visited:
            visited.add((ni, nj))
            if d == (direction + 3) % 4:
                print('L', end='')
            if d == (direction + 1) % 4:
                print('R', end='')
            if d == direction and s:
                print('A', end='')
                s = 0
            else:
                s += 1
            find_route(ni, nj, d, s)


H, W = map(int, input().split())
matrix = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if matrix[i][j] == "#":
            # 시작점 찾기
            si, sj, direction = 0, 0, 0
            visited = {(i, j)}
            find_start(i, j)

            # 경로찾기
            route = []
            visited = {(si, sj)}
            print(si + 1, sj + 1)
            direction_str = ['>', 'v', '<', '^']
            print(direction_str[direction])
            find_route(si, sj, direction, 0)
            exit(0)