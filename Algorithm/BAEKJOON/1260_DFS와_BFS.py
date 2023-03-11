from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for m in range(M):
    sn, en = map(int, input().split())
    graph[sn].append(en)
    graph[en].append(sn)

Q = deque()
Q.extend(sorted(graph[V]))
visited = [V]
dfs = [str(V)]
while Q:
    for q in range(len(Q)):
        now = Q.popleft()
        if now not in visited:
            visited.append(now)
            dfs.append(str(now))
            Q.extendleft(sorted(graph[now], reverse=True))

Q = deque()
Q.extend(sorted(graph[V]))
visited = [V]
bfs = [str(V)]
while Q:
    for q in range(len(Q)):
        now = Q.popleft()
        if now not in visited:
            visited.append(now)
            bfs.append(str(now))
            Q.extend(sorted(graph[now]))

print(' '.join(dfs))
print(' '.join(bfs))
