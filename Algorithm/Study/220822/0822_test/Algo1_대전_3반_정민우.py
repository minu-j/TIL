for tc in range(int(input())):
    N = int(input())
    si, sj, ei, ej = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 목표 지역의 평균값 구하기
    sum_area = 0

    for i in range(si, ei + 1):
        for j in range(sj, ej + 1):
            sum_area += matrix[i][j]

    avr = sum_area // ((ei - si + 1) * (ej - sj + 1))

    # 목표 지역의 각 값과 평균값의 차이 구하기

    ans = 0

    for i in range(si, ei + 1):
        for j in range(sj, ej + 1):
            if matrix[i][j] > avr:              # 해당 좌표의 값이 평균보다 크다면 해당 값 - 평균
                ans += (matrix[i][j] - avr)
            elif matrix[i][j] < avr:            # 해당 좌표의 값이 평균보다 작다면 평균 - 해당 값
                ans += (avr - matrix[i][j])

    print(f'#{tc + 1} {ans}')
