from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

direction = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}

N, M, R = map(int, input().split())
board = {}
for i in range(1, N + 1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, M + 1):
        board[(i, j)] = [row[j], 'S']

ans = 0

for turn in range(R):
    Ay, Ax, D = map(str, input().split())
    Ay, Ax = int(Ay), int(Ax)
    if board[(Ay, Ax)][1] == 'S':
        q = deque([(Ay, Ax)])
        while q:
            now = q.popleft()
            if board[now][1] == "S":
                board[now][1] = "F"
                ans += 1
                ny, nx = now
                for _ in range(board[now][0] - 1):
                    ny = ny + direction[D][0]
                    nx = nx + direction[D][1]
                    if 0 < ny <= N and 0 < nx <= M:
                        if board[(ny, nx)][1] == "S":
                            q.append((ny, nx))

    Dy, Dx = map(int, input().split())
    board[(Dy, Dx)][1] = 'S'

print(ans)
for i in range(1, N + 1):
    for j in range(1, M):
        print(board[(i, j)][1], end=' ')
    print(board[(i, M)][1])
