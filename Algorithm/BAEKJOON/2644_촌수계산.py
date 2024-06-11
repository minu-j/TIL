from collections import deque

N = int(input())
A, B = map(int, input().split())
M = int(input())
matrix = [[] for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

q, visited, ans = deque([A]), set(), 0

while q:
    for i in range(len(q)):
        now = q.popleft()
        if now == B:
            print(ans)
            exit(0)
        visited.add(now)
        for j in matrix[now]:
            if j not in visited:
                q.append(j)
    ans += 1
print(-1)