# # 퀸이 들어갈 수 있는 경우의 수를 구하는 함수
# def queen(n, depth):
#     global ans
#     if depth == n:      # 안겹치고 N까지 왔다면, 정답 +1
#         ans += 1
#         return
#     for now in range(n):        # 순열 재귀함수 응용
#         if not check[depth][now]:          # 해당 행에 퀸을 놓을 자리가 있다면
#             check_mark(n, depth, now, 1)    # 상하좌우, 대각선 +1을 하고
#             queen(n, depth + 1)             # 그 다음 행에 퀸을 놓으러 감
#             check_mark(n, depth, now, -1)   # 다녀왔다면 다시 상하좌우, 대각선 -1해주기
#
#
# # 체스판의 크기와 좌표를 입력하면 check리스트의 해당 좌표의 상하좌우, 대각선에 특정 값을 더해주는 함수
# def check_mark(n, x, y, mark):
#     check[x][y] = 1                     # 일단 해당 위치를 1로 만들고,
#     for i in range(n):
#         for j in range(n):
#             if x - i == y - j:          # 우하향하는 대각선에 +1
#                 check[i][j] += mark
#             elif x + y == i + j:        # 우상향하는 대각선에 +1
#                 check[i][j] += mark
#             elif x == i or y == j:      # 가로, 세로에도 +1
#                 check[i][j] += mark
#
#
# for tc in range(int(input())):
#     N = int(input())
#     sel = [0] * N
#     check = [[0] * N for _ in range(N)]   # 체크 배열을 2차원으로 만들기
#     ans = 0
#     queen(N, 0)
#     print(f'#{tc + 1} {ans}')

####################################################################################

def queen(depth):
    global ans

    if depth == N:
        ans += 1
        return

    for i in range(N):
        if not check[i]:   # 해당 열에 퀸이 있는지 체크

            # 대각선 델타 체크
            flag = True   # 대각선에 퀸이 있는지 없는지 확인용
            for di, dj in (-1, -1), (-1, 1):   # 위에서 아래로 순서대로 마킹하므로, 왼쪽 위, 오른쪽 위 대각선만 확인하면 됨.
                y, x = depth, i
                while flag:
                    if 0 <= y + di < N and 0 <= x + dj < N:
                        y += di
                        x += dj
                        if sel[y][x]:   # 위쪽 대각선에 이미 퀸이 있으면 돌릴 필요 없음.
                            flag = False
                    else:
                        break
            if flag:   # 퀸이 없으면
                check[i] = 1
                sel[depth][i] = 1
                queen(depth + 1)   # 다음행으로 이동
                check[i] = 0
                sel[depth][i] = 0


for tc in range(int(input())):
    N = int(input())

    ans = 0
    check = [0] * N
    sel = [[0] * N for _ in range(N)]
    queen(0)

    print(f'#{tc + 1} {ans}')
