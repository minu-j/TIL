for tc in range(int(input())):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    # 파리채로 때리는 범위의 왼쪽 위 꼭지점을 잡아주고, 모두 순회한다
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 파리채로 때리는 범위 안쪽을 순회하면서 파리의 수를 모두 더한다.
            kill = 0
            for x in range(M):
                for y in range(M):
                    kill += matrix[i + x][j + y]

            # 만약 파리의 수 합이 최대값보다 크면 변수에 저장하여 출력한다.
            if max_kill < kill:
                max_kill = kill
    print(f'#{tc + 1} {max_kill}')
