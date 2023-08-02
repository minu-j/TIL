from collections import deque

LIMIT = 10**5 + 1
N, K = map(int, input().split())
visited = [-1] * LIMIT
q = deque([N])
while q:
    for _ in range(len(q)):
        X = q.popleft()
        if X == K:
            log = []
            while True:
                log.append(X)
                if X == N:
                    break
                parent = visited[X]
                X = parent
            print(len(log) - 1)
            print(' '.join(map(str, log[::-1])))
            exit(0)
        for x in [X - 1, X + 1, 2 * X]:
            if 0 <= x < LIMIT and visited[x] == -1:
                visited[x] = X
                q.append(x)
