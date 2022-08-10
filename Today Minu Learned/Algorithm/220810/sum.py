for tc in range(10):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0   # 최대값을 저장할 변수 생성

    for i in range(100):
        sum_num = 0   # 각 합을 저장할 변수 생성
        for j in range(100):
            sum_num += arr[i][j]   # 가로줄의 합을 구한 후
            if sum_num > max_sum:   # 합이 최대값보다 크다면?
                max_sum = sum_num   # 최대값에 해당 값을 저장
        sum_num = 0
        for j in range(100):
            sum_num += arr[j][i]   # 세로줄의 합도 동일
            if sum_num > max_sum:
                max_sum = sum_num
        sum_num = 0
        for j in range(100):
            if i == j:
                sum_num += arr[i][j]   # 우하향 대각선은 i와 j값이  같은 좌표의 합
                if sum_num > max_sum:
                    max_sum = sum_num
        for j in range(100):
            if i + j == 100:
                sum_num += arr[i][j]   # 우상향 대각선은 i와 j값의 합이 100이 되는 좌표의 합
                if sum_num > max_sum:
                    max_sum = sum_num

    print(f'#{tc + 1} {max_sum}')