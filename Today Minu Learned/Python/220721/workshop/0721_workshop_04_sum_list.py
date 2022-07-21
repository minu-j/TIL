def all_list_sum(list):
    sum_list = 0

    for i in range(len(list)):
        for x in range(len(list[i])):
            sum_list += list[i][x]
    print(sum_list)

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) # => 55