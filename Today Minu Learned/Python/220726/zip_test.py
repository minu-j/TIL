# 2차원 배열 리스트를 만드는 방법

matrix_1 = [[0] * 3] * 3
print(matrix_1)

matrix_2 = []
for _ in range(3):
    matrix_2.append([0] * 3)
print(matrix_2)

matrix_3 = [[0]*3 for _ in range(3)]
print(matrix_3)

matrix_1[0][0] = 9
print(matrix_1)

matrix_2[0][0] = 9
print(matrix_2)

matrix_3[0][0] = 9
print(matrix_3)

print('---------------------------------')

# 2차원 배열 리스트가 정방형일 때 전치하는 법

a = [[3, 1, 2],
[4, 7, 9], 
[6, 8, 5]]
print(a)

for r in range(3):
    for c in range(3):
        if r > c:
            a[r][c], a[c][r] = a[c][r], a[r][c]
print(a)

print('---------------------------------')

# 2차원 배열 리스트가 정방형이 아닐 때 zip을 이용하여 전치하는 법

transposed_matrix = list(zip(*a)) # 튜플
print(transposed_matrix)

transposed_matrix = list(map(list, zip(*a))) # 리스트
print(transposed_matrix)