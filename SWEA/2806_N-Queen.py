# 퀸이 들어갈 수 있는 경우의 수를 구하는 함수
def queen(n, depth):
    global ans
    if depth == n:      # 안겹치고 N까지 왔다면, 정답 +1
        ans += 1
        return
    for now in range(n):        # 순열 재귀함수 응용
        if not check[depth][now]:          # 해당 행에 퀸을 놓을 자리가 있다면
            check_mark(n, depth, now, 1)    # 상하좌우, 대각선 +1을 하고
            queen(n, depth + 1)             # 그 다음 행에 퀸을 놓으러 감
            check_mark(n, depth, now, -1)   # 다녀왔다면 다시 상하좌우, 대각선 -1해주기


# 체스판의 크기와 좌표를 입력하면 check리스트의 해당 좌표의 상하좌우, 대각선에 특정 값을 더해주는 함수
def check_mark(n, x, y, mark):
    check[x][y] = 1                     # 일단 해당 위치를 1로 만들고,
    for i in range(n):
        for j in range(n):
            if x - i == y - j:          # 우하향하는 대각선에 +1
                check[i][j] += mark
            elif x + y == i + j:        # 우상향하는 대각선에 +1
                check[i][j] += mark
            elif x == i or y == j:      # 가로, 세로에도 +1
                check[i][j] += mark


for tc in range(int(input())):
    N = int(input())
    sel = [0] * N
    check = [[0] * N for _ in range(N)]   # 체크 배열을 2차원으로 만들기
    ans = 0
    queen(N, 0)
    print(f'#{tc + 1} {ans}')
