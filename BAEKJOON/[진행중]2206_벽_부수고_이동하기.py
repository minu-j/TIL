N, M = map(int, input().split())
matrix = []
for i in range(N):
    row = []
    for j in input():
        row.append([int(j), 1, 1])
    matrix.append(row)
print(matrix)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
crush = True
stack = [(0, 0)]
visited = {(0, 0)}

while stack:
    now = stack.pop()

    print('now', now)
    if now == (N - 1, M - 1):
        print('goal')
        continue

    if now == (9999, 9999):
        print('checkpoint')
        crush = True

    for d in range(4):
        ny = now[0] + di[d]
        nx = now[1] + dj[d]
        if 0 <= ny < N and 0 <= nx < M:
            if matrix[now[0]][now[1]][0] + 1 < matrix[ny][nx][0]:
                visited.add((ny, nx))
                stack.append((ny, nx))

    print('stack', stack)
    print('visited', visited)