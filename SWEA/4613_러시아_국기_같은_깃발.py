for tc in range(int(input())):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    line_list = []

    ans = 999999999999999999        # 최솟값을 찾아야 하기 때문에 정답은 일단 제일 큰 수로

    # 위에서부터 흰색, 파란색, 빨간색 줄을 채우는 경우의 수 구하기
    for w in range(1, N - 1):
        for b in range(1, N - 1):
            for r in range(1, N - 1):

                # 만약 흰줄, 파란줄, 빨간줄의 합이 N과 같다면 각 줄을 확인한다.
                if w + b + r == N:
                    count = 0
                    for i in matrix[:w]:                    # 흰색으로 칠해야 하는 줄을 돌면서 W가 아닌 문자 갯수
                        count += len(i) - i.count('W')
                    for j in matrix[w:w + b]:               # 파란색으로 칠해야 하는 줄을 돌면서 B가 아닌 문자 갯수
                        count += len(j) - j.count('B')
                    for k in matrix[w + b:]:                # 파란색으로 칠해야 하는 줄을 돌면서 R이 아닌 문자 갯수
                        count += len(k) - k.count('R')
                    if ans > count:       # 모두 더한 값이 정답 값보다 작다면
                        ans = count       # 최솟값을 정답에 할당

    print(f'#{tc + 1} {ans}')
