T = int(input())

for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = income = 0

    for i in range(N - 1, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
            continue
        else:
            income += max_price - price[i]

    print(f'#{tc + 1} {income}')