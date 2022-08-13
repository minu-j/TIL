T = int(input())

for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    start_day = 0
    end_day = N - 1
    income = 0
    day_count = 0
    last_price = price[end_day]
    sum_price = []

    for i in range(end_day, start_day, -1):
        print(price[i])
        # if last_price >= price[i]:
        #     sum_price.append(price[i])
        # elif last_price < price[i]:




    # print(f'#{tc + 1} {income}')