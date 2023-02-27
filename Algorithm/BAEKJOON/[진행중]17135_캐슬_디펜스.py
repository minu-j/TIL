from collections import deque

di = [0, 0, -1]
dj = [-1, 1, 0]


# 위치와 거리가 주어지면 죽인 적의 좌표를 반환하는 함수
def kill(x, y, d):
    global board

    if board[x][y] == 1:
        return x, y

    elif board[x][y] == 0:
        d -= 1
        queue = deque()
        queue.append((x, y))
        visit = set()

        while queue:
            if d == 0:
                return False

            for fi in range(len(queue)):
                now = queue.popleft()

                if now not in visit:
                    visit.add(now)

                for fj in range(3):
                    if board[now[0] + di[fj]][now[1] + dj[fj]] == 1:
                        return now[0] + di[fj], now[1] + dj[fj]

                    elif board[now[0] + di[fj]][now[1] + dj[fj]] == 0:
                        queue.append((now[0] + di[fj], now[1] + dj[fj]))

            d -= 1
        return False


def arrow_position(idx):
    global arrow
    if idx == M:
        if sum(check) == 3:
            A = []
            for idx_, _ in enumerate(check):
                if _:
                    A.append(idx_ + 1)
            arrow.append(A)

        return

    check[idx] = 0
    arrow_position(idx + 1)

    check[idx] = 1
    arrow_position(idx + 1)


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board.insert(0, [2] * M)
for _ in board:
    _.insert(0, 2)
    _.append(2)

check = [0] * M

backup = []
for i in board:
    backup.append(i[::])

ans = 0

arrow = []

arrow_position(0)

for arrows in arrow:
    board = []
    for i in backup:
        board.append(i[::])
    kill_count = 0
    for turn in range(N):
        attack = []

        attack.append(kill(N, arrows[0], D))
        attack.append(kill(N, arrows[1], D))
        attack.append(kill(N, arrows[2], D))

        attacked = set()
        for i in attack:
            if i not in attacked and i is not False:
                attacked.add(i)
                kill_count += 1
                board[i[0]][i[1]] = 0

        board.pop()
        board.insert(0, [2] * (M + 2))

    if kill_count > ans:
        ans = kill_count

print(ans)