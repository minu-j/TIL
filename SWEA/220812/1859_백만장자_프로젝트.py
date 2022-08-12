T = int(input())

for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    price.append(0)
    start_day = 0
    end_day = N
    income = 0
    day_count = 0

    while True:
        max_price = 0
        for i in range(start_day, end_day):
            print(i)
            if max_price < price[i]:
                max_day = i
                max_price = price[i]

        income += max_price * max_day - sum(price[start_day:max_day])
        print('상한가', max_day, max_price, income)
        start_day = max_day + 1
        if start_day == N:
            break

    # print(f'#{tc + 1} {income}')