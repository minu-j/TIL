direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

block = {1: {0: 2, 1: 3, 2: 1, 3: 0},
         2: {0: 1, 1: 3, 2: 0, 3: 2},
         3: {0: 3, 1: 2, 2: 0, 3: 1},
         4: {0: 2, 1: 0, 2: 3, 3: 1},
         5: {0: 2, 1: 3, 2: 0, 3: 1}}


# def play(sy, sx, y, x, d, point, pass_start):
#     global ans
#
#     if (y, x, d, point) in visited:
#         return
#     else:
#         visited.add((y, x, d, point))
#
#     if y == sy and x == sx:
#         if pass_start:
#             pass_start -= 1
#         else:
#             if point > ans:
#                 ans = point
#             return
#     # 경기장을 벗어나지 않는다면
#     if 0 <= y + direction[d][0] < N and 0 <= x + direction[d][1] < N:
#
#         # 다음칸이 빈칸이면
#         if board[y + direction[d][0]][x + direction[d][1]] == 0:
#             play(sy, sx, y + direction[d][0], x + direction[d][1], d, point, pass_start)
#
#         # 다음칸이 블록이면
#         elif 1 <= board[y + direction[d][0]][x + direction[d][1]] <= 5:
#             cd = block[board[y + direction[d][0]][x + direction[d][1]]][d]
#             play(sy, sx, y + direction[d][0], x + direction[d][1], cd, point + 1, pass_start)
#
#         # 다음칸이 웜홀이면
#         elif 6 <= board[y + direction[d][0]][x + direction[d][1]] <= 10:
#             wy = y + direction[d][0]
#             wx = x + direction[d][1]
#             wy2, wx2 = worm_hole[board[y + direction[d][0]][x + direction[d][1]]][(wy, wx)]
#             play(sy, sx, wy2, wx2, d, point, pass_start)
#
#         # 다음칸이 블랙홀이면
#         elif board[y + direction[d][0]][x + direction[d][1]] == -1:
#             if point > ans:
#                 ans = point
#             return
#
#     # 벽에 부딪친다면 5번 블록과 동일한 효과
#     else:
#         cd = block[5][d]
#         play(sy, sx, y + direction[d][0], x + direction[d][1], cd, point + 1, pass_start)


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    start_point = set()
    worm_hole = {}
    ans = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:   # 시작포인트 줍기
                start_point.add((i, j))
            elif 6 <= board[i][j] <= 10:   # 웜홀 짝지어주기
                if board[i][j] not in worm_hole:
                    worm_hole[board[i][j]] = (i, j)
                else:
                    s = worm_hole[board[i][j]][0], worm_hole[board[i][j]][1]
                    e = (i, j)
                    worm_hole[board[i][j]] = {s: e, e: s}

    visited = set()

    for si, sj in start_point:
        for sd in range(4):
            if (si, sj, sd) not in visited:
                # play(si, sj, si, sj, sd, 0, 1)
                sy, sx, y, x, d, point, pass_start = si, sj, si, sj, sd, 0, 1
                flag = True
                while flag:
                    # print(y, x, d, point, pass_start)
                    if (y, x, d, point) in visited:
                        Flag = False
                    else:
                        visited.add((y, x, d, point))

                    if y == sy and x == sx:
                        if pass_start:
                            pass_start -= 1
                        else:
                            if point > ans:
                                ans = point
                            flag = False
                    # 경기장을 벗어나지 않는다면
                    if 0 <= y + direction[d][0] < N and 0 <= x + direction[d][1] < N:

                        # 다음칸이 빈칸이면
                        if board[y + direction[d][0]][x + direction[d][1]] == 0:
                            sy, sx, y, x, d, point, pass_start = sy, sx, y + direction[d][0], x + direction[d][1], d, point, pass_start

                        # 다음칸이 블록이면
                        elif 1 <= board[y + direction[d][0]][x + direction[d][1]] <= 5:
                            cd = block[board[y + direction[d][0]][x + direction[d][1]]][d]
                            sy, sx, y, x, d, point, pass_start = sy, sx, y + direction[d][0], x + direction[d][1], cd, point + 1, pass_start

                        # 다음칸이 웜홀이면
                        elif 6 <= board[y + direction[d][0]][x + direction[d][1]] <= 10:
                            wy = y + direction[d][0]
                            wx = x + direction[d][1]
                            wy2, wx2 = worm_hole[board[y + direction[d][0]][x + direction[d][1]]][(wy, wx)]
                            sy, sx, y, x, d, point, pass_start = sy, sx, wy2, wx2, d, point, pass_start

                        # 다음칸이 블랙홀이면
                        elif board[y + direction[d][0]][x + direction[d][1]] == -1:
                            if point > ans:
                                ans = point
                            flag = False

                    # 벽에 부딪친다면 5번 블록과 동일한 효과
                    else:
                        cd = block[5][d]
                        sy, sx, y, x, d, point, pass_start = sy, sx, y + direction[d][0], x + direction[d][1], cd, point + 1, pass_start

    print(f'#{tc + 1} {ans}')