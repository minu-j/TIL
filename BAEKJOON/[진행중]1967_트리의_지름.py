from heapq import *
from pprint import pprint

N = int(input())
last_child = set(range(1, N + 1))
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(N - 1):
    S, E, W = map(int, input().split())
    matrix[S][E] = matrix[E][S] = W
    if S in last_child:
        last_child.remove(S)

# 뒤에서부터 dp로 거리 더하고, 끝부분만 확인하기
for node in range(N, 0, -1):
    print(matrix[node])