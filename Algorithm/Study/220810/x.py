arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_num = 0

for i in range(3):
    for j in range(3):
        if i == j:
            sum_num += arr[i][j]
            continue
        if i + j == 2:
            sum_num += arr[i][j]
print(sum_num)