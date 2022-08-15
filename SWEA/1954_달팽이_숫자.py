T = int(input())

for tc in range(T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    if N % 2 == 1: # 어차피 정 가운데는 N의 제곱이므로 미리 정해주고 시작
        snail[N // 2][N // 2] = N ** 2

    for lap in range((N // 2)): # 한바퀴 돌때마다 위, 오른쪽, 아래, 왼쪽 방향으로 채워나가기
        for i in range(N - (lap * 2)):
            if lap == 0:                      # 만약 첫번째 바퀴라면
                snail[lap][i + lap] = i + 1   # 일단 1 ~ N까지로 첫번째 줄은 채우기
            else:
                snail[lap][i + lap] = snail[lap][lap - 1] + i + 1   # 아니라면 바로 왼쪽값을 참조하여 +1씩 하기
        for i in range(N - ((lap + 1) * 2)):   # 오른쪽 면을 채우려면 바로 위에있는 값 참조하여 +1
            snail[lap + i + 1][N - 1 - lap] = snail[lap + i][N - 1 - lap] + 1

        for i in range(N - (lap * 2)):   # 아랫면 채울때도 동일
            snail[N - 1 - lap][(N - 1 - i) - lap] = i + 1 + snail[N - 1 - lap - 1][N - 1 - lap]

        for i in range(N - ((lap + 1) * 2)):   # 왼쪽면 채울때도 동일
            snail[N - (lap + i + 2)][lap] = snail[N - (lap + i + 1)][lap] + 1

            # 다 채워질때까지 반복

    print(f'#{tc + 1}')   # 출력을 어떻게 할지에서 2차 난관....
    for i in range(N):
        for j in range(N):   # 이렇게 하는게 맞는지는 모르겠지만 출력도 2중 for문 사용해서
            if j == N - 1:   # 리스트 마지막 행일 때 엔터
                print(snail[i][j])
            else:   # 리스트 이어지는 것들은 띄어쓰기만 포함해서 출력
                print(snail[i][j], end=' ')