def min_sum(n, depth):
    global min_num

    # 백트래킹 - 지금까지 선택 합계가 최소 합보다 크다면 더이상 진행할 필요가 없으므로 리턴
    if sum(sel) >= min_num:
        return

    # n만큼 단계로 들어갔을 경우, 합계가 최소 합보다 작으면 최소 합 변수 갱신
    if depth == n:
        if sum(sel) < min_num:
            min_num = sum(sel)
        return

    # 재귀 순열
    for i in range(n):
        if not check[i]:
            sel[depth] = matrix[depth][i]
            check[i] = 1
            min_sum(n, depth + 1)
            check[i] = 0
            sel[depth] = 0   # 백트래킹을 위해서 재귀를 빠져나올 때 선택된 숫자도 초기화


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    sel = [0] * N
    check = [0] * N

    min_num = 999999999

    min_sum(N, 0)

    print(f'#{tc + 1} {min_num}')
