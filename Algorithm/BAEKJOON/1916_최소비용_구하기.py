from heapq import *


def ds():
    dist = [9999999999] * (N + 1)
    visited = set()
    heap = []
    heappush(heap, (0, S))

    while heap:
        cost, node = heappop(heap)
        if node not in visited:
            dist[node] = cost
            visited.add(node)

            for destination in range(N + 1):
                if destination not in visited and dist[destination] > matrix[node][destination] + dist[node]:
                    heappush(heap, (matrix[node][destination] + dist[node], destination))
    return dist[E]


N = int(input())
M = int(input())
matrix = [[9999999999] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    if matrix[s][e] > c:
        matrix[s][e] = c
S, E = map(int, input().split())
print(ds())
