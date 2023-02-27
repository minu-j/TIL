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


N = int(input())

ans = 0
check = [0] * N
sel = [[0] * N for _ in range(N)]
queen(0)

print(ans)