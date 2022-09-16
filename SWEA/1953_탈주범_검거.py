# 데크로 풀기
from collections import deque

# 각 터널 번호별로 갈 수 있는 방향 지정해주기 - 딕셔너리 활용
tunnels = {1: (('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)),
           2: (('up', -1, 0), ('down', 1, 0)),
           3: (('left', 0, -1), ('right', 0, 1)),
           4: (('up', -1, 0), ('right', 0, 1)),
           5: (('down', 1, 0), ('right', 0, 1)),
           6: (('down', 1, 0), ('left', 0, -1)),
           7: (('up', -1, 0), ('left', 0, -1))}


# 가고싶은 터널로 이동 가능한지 확인하는 함수
def is_move_possible(p, direct, x, y):
    if 0 <= p[0] + x < N and 0 <= p[1] + y < M:                       # matrix범위 내에 있고,
        if matrix[p[0] + x][p[1] + y]:                                # 그 위치에 터널이 있고,
            if is_not_blocked(direct, matrix[p[0] + x][p[1] + y]):    # 막혀있지 않다면?
                return True                                           # 갈 수 있다.


# 그 위치에 터널이 있긴 한데.. 막혀있지 않은지 확인하기
def is_not_blocked(d, t):
    if d == 'up':
        if t == 3 or t == 4 or t == 7:   # 예) 3, 4, 7번 터널은
            return False                 # 아래가 막혀있어서 위로는 못온다.
        else:
            return True
    elif d == 'down':
        if t == 3 or t == 5 or t == 6:
            return False
        else:
            return True
    elif d == 'left':
        if t == 2 or t == 6 or t == 7:
            return False
        else:
            return True
    elif d == 'right':
        if t == 2 or t == 4 or t == 5:
            return False
        else:
            return True


for tc in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # BFS로 풀기
    queue = deque([(R, C)])
    visited = set()   # visited는 순서 상관 없으므로 셋으로 하기
    time = L

    # 남은 시간이 0이 될 때 까지 반복하기
    while time:

        # 한 시간마다 갈 수 있는 거리만큼 끊어서 시간 카운트하기
        for a_time in range(len(queue)):
            now = queue.popleft()
            if now not in visited:   # 방문한 적 없으면 방문하기
                visited.add(now)

                # 해당하는 터널이 갈 수 있는 방향대로 델타탐색
                for direction, i, j in tunnels[matrix[now[0]][now[1]]]:
                    if is_move_possible(now, direction, i, j):   # 해당 터널로 이동할 수 있는지 확인하고
                        queue.append((now[0] + i, now[1] + j))   # 갈 수 있다면 큐에 추가하기
        time -= 1   # 한 시간 지났으니까 시간 -1

    # 그동안 방문했던 터널 갯수가 정답이 될 것임.
    print(f'#{tc + 1} {len(visited)}')
