def dijkstra():
    dist = [99] * (N + 1)
    dist[0] = 0
    visited = [False] * (N + 1)

    for i in range(N + 1):
        min_idx = -1
        min_value = 99

        for j in range(N + 1):
            if not visited[j] and dist[j] < min_value:
                min_idx = j
                min_value = dist[j]

        visited[min_idx] = True

        for k in range(N + 1):
            if not visited[k] and dist[k] > matrix[min_idx][k] + dist[min_idx]:
                dist[k] = matrix[min_idx][k] + dist[min_idx]

    return dist[N]


for tc in range(int(input())):
    N, E = map(int, input().split())

    matrix = [[99] * (N + 1) for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        matrix[s][e] = w

    print(f'#{tc + 1} {dijkstra()}')
