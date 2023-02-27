def move(depth):
    global ans

    if depth == N:

        # 해당 경로 값의 합 구하기
        sum_num = 0
        for i in range(N):
            sum_num += matrix[sel[i]][sel[i + 1]]

        if ans > sum_num:
            ans = sum_num
        return

    # 중복되지 않게 장소 순서를 주워담기
    for i in place:
        if i not in sel:
            sel[depth] = i
            move(depth + 1)
            sel[depth] = 0


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    place = list(range(1, N))   # 0번을 출발/도착이라고 했을 때 방문할 장소는 1부터 N - 1번
    sel = [0] * (N + 1)         # 앞뒤에 0번을 붙일것이므로 N + 1 길이의 리스트 생성
    ans = 99999999999999999999999
    move(1)                     # 시작점을 0으로 두고, 1번칸부터 시작

    print(f'#{tc + 1} {ans}')
