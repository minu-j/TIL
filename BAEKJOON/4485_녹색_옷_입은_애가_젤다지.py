# def move(y, x, count):
#     global ans
#
#     if y == x == (N - 1):
#         if count < ans:
#             ans = count
#         return
#
#     for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
#         if (y + i, x + j) not in visited and 0 <= y + i < N and 0 <= x + j < N and (count + matrix[y + i][x + j] < ans):
#             visited.append((y + i, x + j))
#             move(y + i, x + j, count + matrix[y + i][x + j])
#             visited.pop()
#
#
# tc = 0
# while True:
#     tc += 1
#     N = int(input())
#     if N == 0:
#         break
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [(0, 0)]
#     ans = 9999999999999999
#     move(0, 0, matrix[0][0])
#
#     print(f'Problem {tc}: {ans}')


def move():
    dist = [[99] * N for _ in range(N)]
    dist[0][0] = matrix[0][0]
    visited = [[False] * N for _ in range(N)]

    for _ in range(N * N):
        min_idx = (-1, -1)
        min_value = 99

        for y in range(N):
            for x in range(N):
                if not visited[y][x] and dist[y][x] < min_value:
                    min_idx = (y, x)
                    min_value = dist[y][x]

        visited[min_idx[0]][min_idx[1]] = True

        for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
            if 0 <= min_idx[0] + i < N and 0 <= min_idx[1] + j < N:
                if not visited[min_idx[0] + i][min_idx[1] + j] and dist[min_idx[0] + i][min_idx[1] + j] > matrix[min_idx[0] + i][min_idx[1] + j] + dist[min_idx[0]][min_idx[1]]:
                    dist[min_idx[0] + i][min_idx[1] + j] = matrix[min_idx[0] + i][min_idx[1] + j] + dist[min_idx[0]][min_idx[1]]

    return dist[N - 1][N - 1]


tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(f'Problem {tc}: {move()}')
