import sys
from collections import deque

def bfs(s, t):
    q = deque([s])
    steps = [set() for _ in range(n + 1)]
    steps[s].add(s)
    while q:
        now = q.popleft()
        for node in graph[now]:
            if now not in steps[node]:
                steps[node].add(now)
                if node != t:
                    q.append(node)
    visited = set()
    rewind = steps[t]
    while rewind:
        add_rewind = set()
        for node in rewind:
            visited.add(node)
            add_rewind |= steps[node]
        rewind |= add_rewind
        rewind -= visited
    return visited

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
S, T = map(int, input().split())

print(len(bfs(T, S) & bfs(S, T)))