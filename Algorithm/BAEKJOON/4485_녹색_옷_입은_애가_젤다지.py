# dfs => 시간초과
#
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
#
################################################################

# 다익스트라
# python  시간초과
# pypy    115880KB  3328ms

def move():
    dist = [[9999999999999999] * N for _ in range(N)]   # 맵이 2차원이니깐 dist도 2차원
    dist[0][0] = matrix[0][0]                           # dist 좌표도 두개
    visited = [[False] * N for _ in range(N)]           # visited도 2차원

    for _ in range(N * N):   # 일반적인 그래프와 다르게, 2차원 배열을 순회해야 하므로 N * N번 반복해야 함.
        min_idx = (-1, -1)                              # index 좌표도 두개
        min_value = 9999999999999999

        # 2차원 배열에서 아직 방문하지 않았고, dist값이 제일 작은 위치 찾기
        for y in range(N):
            for x in range(N):
                if not visited[y][x] and dist[y][x] < min_value:
                    min_idx = (y, x)
                    min_value = dist[y][x]

        visited[min_idx[0]][min_idx[1]] = True

        # 방문한 해당 min_index 위치에서 상하좌우 한칸씩 사방탐색하기
        for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
            if 0 <= min_idx[0] + i < N and 0 <= min_idx[1] + j < N:
                if not visited[min_idx[0] + i][min_idx[1] + j] and dist[min_idx[0] + i][min_idx[1] + j] > matrix[min_idx[0] + i][min_idx[1] + j] + dist[min_idx[0]][min_idx[1]]:
                    if matrix[min_idx[0] + i][min_idx[1] + j] < dist[N - 1][N - 1]:   # 도착점보다 이미 커져버리면 가지 않기(0.3초 단축)
                        dist[min_idx[0] + i][min_idx[1] + j] = matrix[min_idx[0] + i][min_idx[1] + j] + dist[min_idx[0]][min_idx[1]]

    return dist[N - 1][N - 1]   # 도착점의 dist값 출력


tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]   # 입력받은 matrix를 인접행렬처럼 사용

    print(f'Problem {tc}: {move()}')

################################################################

# heapq를 이용한 다익스트라
# python  34444KB  288ms
# pypy   120576KB  288ms

import heapq


def move():
    dist = [[9999999999999999] * N for _ in range(N)]
    visited = set()
    heap = []
    heapq.heappush(heap, (matrix[0][0], (0, 0)))

    while heap:
        rupee, p = heapq.heappop(heap)
        dist[p[0]][p[1]] = rupee
        visited.add(p)

        for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
            if 0 <= p[0] + i < N and 0 <= p[1] + j < N:
                if (p[0] + i, p[1] + j) not in visited and dist[p[0] + i][p[1] + j] > matrix[p[0] + i][p[1] + j] + rupee:
                    dist[p[0] + i][p[1] + j] = matrix[p[0] + i][p[1] + j] + rupee
                    heapq.heappush(heap, (matrix[p[0] + i][p[1] + j] + rupee, (p[0] + i, p[1] + j)))
    return dist[N - 1][N - 1]


tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]   # 입력받은 matrix를 인접행렬처럼 사용

    print(f'Problem {tc}: {move()}')