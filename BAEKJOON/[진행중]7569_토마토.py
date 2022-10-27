import sys
input = sys.stdin.readline

# 1차원으로
# direction = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0))
dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

red = set()
green = set()

for h in range(H):
    for n in range(N):
        tomatoes = list(map(int, input().split()))
        for m in range(M):
            if tomatoes[m] == 1:
                red.add((h, n, m))
            elif tomatoes[m] == 0:
                green.add((h, n, m))

day = 0
yellow = set()
ans = 0
visited = set()

while True:
    for h, n, m in red:
        if (h, n, m) not in visited:
            visited.add((h, n, m))
            for d in range(6):
                x = m + dx[d]
                y = n + dy[d]
                z = h + dz[d]
                if 0 <= z < H and 0 <= y < N and 0 <= x < M:
                    if (z, y, x) in green:
                        yellow.add((z, y, x))
                        green.remove((z, y, x))

    if green and not yellow:
        print(-1)
        exit(0)

    elif not green and not yellow:
        print(day)
        exit(0)

    else:
        red |= yellow
        # for y in yellow:
        #     red.add(y)
        yellow = set()

    day += 1
