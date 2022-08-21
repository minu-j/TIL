for tc in range(int(input())):
    num = list(map(int, input().split()))
    ans = 0

    for i in range(1 << len(num)):

        sum_num = 0

        for j in range(len(num)):
            if i & (1 << j):
                sum_num += num[j]

        if i > 0 and sum_num == 0:
            ans = 1

    print(f'#{tc + 1} {ans}')


