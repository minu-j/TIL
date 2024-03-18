# 완전탐색
# 각 좌표마다 상, 하, 좌, 우, 대각선 8방향을 5칸씩 확인하며 1 또는 2가 5개 이상 나열되었는지 확인한다.
# 가능? -> 19 * 19 좌표를 8번씩 5+1칸 확인하므로 완탐 충분.

# 가장 왼쪽(세로는 가장 위) 좌표만 출력하므로, 출력되어야하는 좌표를 시작지점으로 하도록 방향 설정
dx, dy = [1, 0, 1, 1], [0, 1, -1, 1]

BOARD_SIZE = 19
board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]


def check_is_five(color, x, y, direction, depth=0):
    if depth == 5:
        # 5개 색이 모두 같은 경우
        return True

    elif 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[y][x] == color:
        # 해당 좌표의 색이 일치하는 경우
        return check_is_five(color, x + dx[direction], y + dy[direction], direction, depth + 1)

    else:
        # 색이 일치하지 않는 경우
        return False


def check_is_not_six(color, x, y, direction):
    prev_x, prev_y = x - dx[direction], y - dy[direction]
    next_x, next_y = x + dx[direction] * 5, y + dy[direction] * 5

    if 0 <= prev_x < BOARD_SIZE and 0 <= prev_y < BOARD_SIZE and board[prev_y][prev_x] == color:
        # 이전 좌표가 바둑판 내에 있고, 색이 같으면 육목 이상임.
        return False

    if 0 <= next_x < BOARD_SIZE and 0 <= next_y < BOARD_SIZE and board[next_y][next_x] == color:
        # 이후 좌표가 바둑판 내에 있고, 색이 같으면 육목 이상임.
        return False

    return True


for y in range(BOARD_SIZE):
    for x in range(BOARD_SIZE):
        color = board[y][x]

        if color:
            for d in range(4):
                if check_is_five(color, x, y, d) and check_is_not_six(color, x, y, d):
                    print(color)
                    print(y + 1, x + 1)
                    exit(0)
print(0)
