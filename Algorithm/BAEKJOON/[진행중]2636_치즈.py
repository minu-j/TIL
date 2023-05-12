from pprint import pprint

# 0, 0부터 그래프 탐색 하면서 공기와의 접촉 판단하기
# 1번 이상 접촉될 경우 녹일 set에 포함
# 그래프 탐색 몇번 돌았는지로 정답 판단

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    visited = {(0, 0)}
    touch = set()
    melt = set()
    wait_list = [(0, 0)]
    while wait_list:
        (y, x) = wait_list.pop()
        for d in range(4):
            ny, nx = y + di[d], x + dj[d]
            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] == 1:
                    if (ny, nx) in touch:
                        melt.add((ny, nx))
                    else:
                        touch.add((ny, nx))
                elif matrix[ny][nx] == 0 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    wait_list.append((ny, nx))
    if len(touch) == 0:
        print(time)
        break
    else:
        for (my, mx) in melt:
            matrix[my][mx] = 0
        time += 1
