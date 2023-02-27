# 델타 좌표 만들고 시작(상, 하, 좌, 우, 대각선)
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


# 팔방을 탐색해서 조건에 맞게 돌을 바꿔주는 함수
def change_stone(pi, pj, c):

    # 조건과 맞는 돌을 일직선으로 이동하며 찾는 함수
    def find_stone(d, pii, pjj):
        if 0 <= pii + di[d] < N and 0 <= pjj + dj[d] < N:

            # 만약 0이 나와버리면 바꿀 돌이 없음.
            if board[pii + di[d]][pjj + dj[d]] == 0:
                return False

            # 같은 색의 돌이 나오면 중간에 있는 돌을 다 바꿔야 함.
            elif board[pii + di[d]][pjj + dj[d]] == c:
                return True

            # 다른 색의 돌이 나오면 바꿀지 말지 모르니까 일단 리스트에 저장해놓기.
            else:
                stones.append((pii + di[d], pjj + dj[d]))
                if find_stone(d, pii + di[d], pjj + dj[d]):
                    return True

    # 팔방 탐색
    for direction in range(8):
        stones = []

        # 돌을 바꿔야 하면 리스트에 저장된 돌들을 바꿔주기
        if find_stone(direction, pi, pj):
            for stone in stones:
                board[stone[0]][stone[1]] = c


for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # 보드에 기본 돌 세팅
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2] = 2

    for turn in range(M):
        Pj, Pi, color = map(int, input().split())

        # 보드의 해당 위치에 돌을 놓고,
        board[Pi - 1][Pj - 1] = color

        # 조건에 맞게 돌 바꾸기
        change_stone(Pi - 1, Pj - 1, color)

    B = 0
    W = 0

    # 각 줄의 검은돌, 흰돌을 찾아서 갯수 세기
    for row in board:
        B += row.count(1)
        W += row.count(2)

    ans = 0
    print(f'#{tc + 1}', B, W)
