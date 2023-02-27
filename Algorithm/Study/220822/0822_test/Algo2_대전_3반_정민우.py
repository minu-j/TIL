for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    target = [list(map(int, input().split())) for _ in range(3)]

    ans = 0

    # 전체 2차원 배열을 순회하는 반복문
    for i in range(N - 2):
        for j in range(N - 2):

            count = 0

            # 해당 좌표를 좌상단 기준으로 하여 3 X 3에 해당하는 구역을 순회하는 반복문
            for x in range(3):
                for y in range(3):
                    if matrix[i + x][j + y] != target[x][y]:    # 효율성을 위해서 찾으려는 숫자와 다른 값이 발견되면
                        count = -1                              # 카운트에 -1을 할당한다.
                    else:
                        count += 1
                if count == -1:                                 # 카운트가 -1이라면 더이상 찾을 필요가 없으므로 반복문을 종료한다.
                    break

            if count == 9:   # 일치하는 값이 9가 되면 정답 +1
                ans += 1

    print(f'#{tc + 1} {ans}')
