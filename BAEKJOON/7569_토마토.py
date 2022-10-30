from collections import deque
import sys
input = sys.stdin.readline

# 1차원으로
# direction = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0))
dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

yellow = deque()
green = set()

for h in range(H):
    for n in range(N):
        tomatoes = list(map(int, input().split()))
        for m in range(M):
            if tomatoes[m] == 1:
                yellow.append((h, n, m))
            elif tomatoes[m] == 0:
                green.add((h, n, m))

day = 0
ans = 0
visited = set()

while True:
    for t in range(len(yellow)):
        now = yellow.popleft()
        if now not in visited:
            visited.add(now)
            for d in range(6):
                x = now[2] + dx[d]
                y = now[1] + dy[d]
                z = now[0] + dz[d]
                if 0 <= z < H and 0 <= y < N and 0 <= x < M:
                    if (z, y, x) in green:
                        yellow.append((z, y, x))
                        green.remove((z, y, x))

    if green and not yellow:
        print(-1)
        exit(0)

    elif not green and not yellow:
        print(day)
        exit(0)

    day += 1
