def dict_list_sum(dict):
    sum_value = 0

    for i in range(len(dict)):
        sum_value += dict[i]['age']
    print(sum_value)

dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]) # => 1