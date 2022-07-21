def list_sum(num):
    sum_num = 0

    for i in range(len(num)):
        sum_num += int(num[i]) # num의 값을 앞에서부터 sum_num에 더함
    print(sum_num)

list_sum([1, 2, 3, 4, 5])