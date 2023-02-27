di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def find_way(fi, fj, h, distance, chance):
    global max_distance

    if distance > max_distance:   # 전보다 더 먼 거리를 가면 최대 거리 갱신
        max_distance = distance

    # 델타 탐색
    for d in range(4):
        if 0 <= fi + di[d] < N and 0 <= fj + dj[d] < N:   # 지도 범위 벗어나지 않게 제한

            if (fi + di[d], fj + dj[d]) not in visited:   # 방문여부 확인
                visited.append((fi + di[d], fj + dj[d]))

                # 가려고 하는 곳이 더 낮은 경우 이동할 수 있음.
                if matrix[fi + di[d]][fj + dj[d]] < h:
                    find_way(fi + di[d],  fj + dj[d], matrix[fi + di[d]][fj + dj[d]], distance + 1, chance)

                # 더 높아도, 산깎기 기회가 있으면 산을 깎고 갈 수 있음.
                elif chance and h <= matrix[fi + di[d]][fj + dj[d]] < h + K:
                    find_way(fi + di[d], fj + dj[d], h - 1, distance + 1, chance - 1)

                visited.pop()   # 다음 재귀를 위해 방문여부 제거


for tc in range(int(input())):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_high = 0
    max_high_set = set()
    max_distance = 0

    # 가장 높은 봉우리 찾기
    for i1 in range(N):
        for j1 in range(N):
            if matrix[i1][j1] >= max_high:
                if matrix[i1][j1] > max_high:
                    max_high_set.clear()
                max_high_set.add((i1, j1))
                max_high = matrix[i1][j1]

    # 가장 높은 봉우리 리스트를 돌면서 최대거리 확인하기
    for hi, hj in max_high_set:
        visited = [(hi, hj)]
        find_way(hi, hj, max_high, 1, 1)

    print(f'#{tc + 1} {max_distance}')
