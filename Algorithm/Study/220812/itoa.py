i = 1
while True:
    num = int(input())
    num_list = []
    while True:
        num_1 = num % 10
        num_list.append(num_1)
        num = num // 10
        if num == 0:
            break

    print(f'#{i} {num}', type(num))
    i += 1