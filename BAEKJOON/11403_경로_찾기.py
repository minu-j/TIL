from pprint import pprint
from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for column in range(N):
        if row != column and matrix[row][column] == 1:
            Q = deque([column])

            while Q:
                now = Q.popleft()
                for now_column in range(len(matrix[now])):
                    if matrix[now][now_column] == 1 and matrix[row][now_column] == 0:
                        matrix[row][now_column] = 1
                        Q.append(now_column)

for ans_row in matrix:
    for ans_column in ans_row:
        print(ans_column, end=' ')
    print()
