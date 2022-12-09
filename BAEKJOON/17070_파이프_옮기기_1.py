from pprint import pprint

# 왼쪽, 위, 왼쪽 위 대각선
di = [0, -1, -1]
dj = [-1, 0, -1]

N = int(input())

# 벽 입력
wall = set()
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            wall.add((i, j))

# [가로, 세로, 대각선] 2차원 공간
matrix = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
matrix[0][1][0] = 1

# 순회 하며 DP
for i in range(N):
    for j in range(N):
        if (i, j) not in wall:  # 해당 위치가 벽이 아닌지 확인
            for d in range(3):  # 방향 순회 하며 확인
                if 0 <= i + di[d] < N and 0 <= j + dj[d] < N:
                    if d == 0:  # 가로 확인할 때
                        matrix[i][j][0] += matrix[i + di[d]][j + dj[d]][0]
                        matrix[i][j][0] += matrix[i + di[d]][j + dj[d]][2]

                    if d == 1:  # 세로 확인할 때
                        matrix[i][j][1] += matrix[i + di[d]][j + dj[d]][1]
                        matrix[i][j][1] += matrix[i + di[d]][j + dj[d]][2]

                    if d == 2:  # 대각선 확인할 때
                        if (i - 1, j) not in wall and (i, j - 1) not in wall:   # 해당 칸 위, 아래도 비어있어야 함
                            matrix[i][j][2] += matrix[i + di[d]][j + dj[d]][0]
                            matrix[i][j][2] += matrix[i + di[d]][j + dj[d]][1]
                            matrix[i][j][2] += matrix[i + di[d]][j + dj[d]][2]

print(sum(matrix[N - 1][N - 1]))