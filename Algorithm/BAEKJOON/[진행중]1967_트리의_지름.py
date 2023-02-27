from heapq import *
from pprint import pprint


def ds(start):
    dist = [99999999] * (N + 1)
    visited = set()
    heap = []
    heappush(heap, (0, start))

    while heap:
        w, node = heappop(heap)
        if node not in visited:
            dist[node] = w
            visited.add(node)

            for destination in range(N + 1):
                if destination not in visited and dist[destination] > matrix[node][destination] + dist[node]:
                    heappush(heap, (matrix[node][destination] + dist[node], destination))
    return dist


N = int(input())
last_child = set(range(1, N + 1))
matrix = [[99999999] * (N + 1) for _ in range(N + 1)]
for _ in range(N - 1):
    S, E, W = map(int, input().split())
    matrix[S][E] = W
    if S in last_child:
        last_child.remove(S)

ans = 0

print(ds(5))