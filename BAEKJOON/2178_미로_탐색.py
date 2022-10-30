import sys
input = sys.stdin.readline

di, dj, i, j = [-1, 0, 1, 0], [0, 1, 0, -1], 0, 0
N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
ans = 99999999999999999999
while True:
    for d in range(4):
        ny = di[d] + i
