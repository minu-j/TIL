from collections import deque

N = int(input())
matrix = [list(input()) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ans = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            matrix[i][j] = '0'
            q = deque([(i, j)])
            count = 1
            while q:
                now = q.popleft()
                for d in range(4):
                    ny = now[0] + di[d]
                    nx = now[1] + dj[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        if matrix[ny][nx] == '1':
                            matrix[ny][nx] = '0'
                            q.append((ny, nx))
                            count += 1
            ans.append(count)
print(len(ans))
for a in sorted(ans):
    print(a)
