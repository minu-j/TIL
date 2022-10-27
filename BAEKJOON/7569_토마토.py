direction = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0))

M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

red = set()
green = set()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                red.add((h, n, m))
            elif tomatoes[h][n][m] == 0:
                green.add((h, n, m))

tomatoes_num = len(red) + len(green)

day = 0
yellow = set()
flag = True
ans = 0
visited = set()
while flag:
    for h, n, m in red:
        if (h, n, m) not in visited:
            visited.add((h, n, m))
            for dz, dy, dx in direction:
                if 0 <= h + dz < H and 0 <= n + dy < N and 0 <= m + dx < M:
                    if tomatoes[h + dz][n + dy][m + dx] == 1:
                        if tomatoes[h + dz][n + dy][m + dx] not in red:
                            red.add((h + dz, n + dy, m + dx))
                    elif tomatoes[h + dz][n + dy][m + dx] == 0:
                        if (h + dz, n + dy, m + dx) not in red:
                            yellow.add((h + dz, n + dy, m + dx))
                            if (h + dz, n + dy, m + dx) in green:
                                green.remove((h + dz, n + dy, m + dx))

    # print(day)
    # print('red', red)
    # print('yellow', yellow)
    # print('green', green)
    if green and not yellow:
        ans = -1
        break

    elif not green and not yellow:
        ans = day
        break

    elif yellow:
        for y in yellow:
            red.add(y)
        yellow.clear()

    day += 1

print(ans)