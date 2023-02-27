from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

M, N = map(int, input().split())

yellow = deque()
green = set()

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            yellow.append((i, j))
        elif row[j] == 0:
            green.add((i, j))

visited = set()
day = 0

while True:
    for t in range(len(yellow)):
        now = yellow.popleft()
        if now not in visited:
            visited.add(now)
            for d in range(4):
                y = now[0] + dy[d]
                x = now[1] + dx[d]
                if 0 <= y < N and 0 <= x < M:
                    if (y, x) in green:
                        yellow.append((y, x))
                        green.remove((y, x))

    if green and not yellow:
        print(-1)
        exit(0)

    elif not green and not yellow:
        print(day)
        exit(0)

    day += 1
