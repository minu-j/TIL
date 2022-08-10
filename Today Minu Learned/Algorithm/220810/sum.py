for tc in range(10):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += arr[i][j]
            if sum_num > max_sum:
                max_sum = sum_num
        sum_num = 0
        for j in range(100):
            sum_num += arr[j][i]
            if sum_num > max_sum:
                max_sum = sum_num

    print(f'#{tc + 1} {max_sum}')