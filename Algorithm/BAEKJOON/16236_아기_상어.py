from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_target(y, x):

    distance = 0
    visited = set()
    target_distance = 999999999
    target = ()
    q = deque()
    q.append((y, x))

    while q:
        for n in range(len(q)):
            now = q.popleft()

            for d in range(4):
                ny = now[0] + dy[d]
                nx = now[1] + dx[d]
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    if 0 <= ny < N and 0 <= nx < N:

                        # 방문한 좌표에 물고기가 있을 때
                        if (ny, nx) in fish:

                            # 상어가 더 높을 때(먹을 수 있음)
                            if fish[(ny, nx)] < level:

                                # 지정된 타겟이 이미 있을 때
                                if target:

                                    # 타겟까지 거리가 기존 타겟 거리와 같다면
                                    if distance + 1 == target_distance:

                                        # 타겟보다 위에 있으면 먹을 수 있음
                                        if ny < target[0]:
                                            target_distance = distance + 1
                                            target = (ny, nx)

                                        # 타켓과 y 위치가 같다면 왼쪽에 있어야 함
                                        elif ny == target[0] and nx < target[1]:
                                            target_distance = distance + 1
                                            target = (ny, nx)

                                        # 타겟보다 오른쪽이나 아래에 있으면 안됨
                                        else:
                                            continue

                                    # 기존 타겟 거리보다 가까우면 바로 먹을 수 있음
                                    elif distance + 1 < target_distance:
                                        target_distance = distance + 1
                                        target = (ny, nx)

                                # 타겟이 없을 때
                                else:
                                    target_distance = distance + 1
                                    target = (ny, nx)

                            # 상어의 레벨이 낮을 때(지나갈수 없음)
                            elif fish[(ny, nx)] > level:
                                continue

                            # 레벨이 같을 때(지나칠 수 있음)
                            elif fish[(ny, nx)] == level:
                                if distance + 1 <= target_distance:   # 타겟보다 가깝다면
                                    q.append((ny, nx))

                        else:
                            if distance + 1 <= target_distance:   # 타겟보다 가깝다면
                                q.append((ny, nx))

        distance += 1

    return target_distance, target


def level_up():
    global level, eat
    if level == eat:
        level += 1
        eat = 0

N = int(input())

level = 2
eat = 0
shark = []
fish = {}
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(N):
        if matrix[i][j] == 9:
            shark = [i, j]
        elif 0 < matrix[i][j] <= 6:
            fish[(i, j)] = matrix[i][j]

time = 0

while True:
    # 목표 찾기
    D, P = find_target(shark[0], shark[1])

    # 타겟이 있다면
    if P:
        # 상어를 해당위치로 이동
        shark = P
        # 물고기 딕셔너리에서 해당좌표 삭제
        fish.pop(P)
        # 시간 흐르기
        time += D
        # 상어 레벨업
        eat += 1
        level_up()

    # 타겟이 없다면
    else:
        break

print(time)