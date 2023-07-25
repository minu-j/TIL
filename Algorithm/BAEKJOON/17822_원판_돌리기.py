from collections import deque

N, M, T = map(int, input().split())
disks = [list(map(int, input().split())) for _ in range(N)]
top = [0] * N

# 1. x의 배수인 원판을 d방향으로 k칸 회전 / d = 0 ? 시계 방향 : 반시계 방향
def rotate(x, d, k):
    for i in range(x - 1, N, x):
        if d:
            disks[i] = disks[i][k:] + disks[i][:k]
        else:
            disks[i] = disks[i][M - k:] + disks[i][:M - k]

# 2. 인접하면서 수가 같은 것을 모두 찾는다.
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def search():
    sum_disk = 0
    count = 0
    remove = 0
    for i in range(N):
        for j in range(M):
            target = disks[i][j]
            visited = set()
            if target:
                q = deque([(i, j)])
                visited.add((i, j))
                while q:
                    now = q.popleft()
                    for di, dj in d:
                        ni, nj = now[0] + di, (M + now[1] + dj) % M
                        if 0 <= ni < N and disks[ni][nj] == target and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            q.append((ni, nj))
            if 1 < len(visited):
                for n, m in visited:
                    disks[n][m] = 0
                    remove += 1
            else:
                if disks[i][j]:
                    sum_disk += disks[i][j]
                    count += 1
    
    if not remove and sum_disk:
        avg = sum_disk / count
        for i in range(N):
            for j in range(M):
                if disks[i][j] and avg < disks[i][j]:
                    disks[i][j] -= 1
                elif disks[i][j] and disks[i][j] < avg:
                    disks[i][j] += 1
    return sum_disk    

for t in range(T):
    rotate(* map(int, input().split()))
    ans = search()
print(ans)

# for _ in range(N):
#     print(_, disks[_][top[_]:] + disks[_][:top[_]])
