import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def section(y, x, m, color):
    m[y][x] = '*'
    visited = set()
    q = deque([(y, x)])
    while q:
        now = q.popleft()
        for d in range(4):
            ny = di[d] + now[0]
            nx = dj[d] + now[1]
            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) not in visited and m[ny][nx] == color:
                    visited.add((ny, nx))
                    m[ny][nx] = ''
                    q.append((ny, nx))


N = int(input())

matrix = []
matrix_RG = []

for i in range(N):
    row = list(input())
    matrix.append(row[:])
    for j in range(N):
        if row[j] == 'G':
            row[j] = 'R'
    matrix_RG.append(row)

count = 0
count_RG = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            section(i, j, matrix, matrix[i][j])
            count += 1
        if matrix_RG[i][j]:
            section(i, j, matrix_RG, matrix_RG[i][j])
            count_RG += 1

print(count, count_RG)