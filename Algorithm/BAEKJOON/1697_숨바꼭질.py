from collections import deque

LIMIT = 10**5 + 1
N, K = map(int, input().split())
visited = set()
q = deque([N])
t = 0
while q:
    for _ in range(len(q)):
        X = q.popleft()
        if X == K:
            print(t)
            exit(0)
        for x in [X - 1, X + 1, 2 * X]:
            if 0 <= x < LIMIT and x not in visited:
                visited.add(x)
                q.append(x)
    t += 1