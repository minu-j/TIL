max = 0
count = 0
for i in range(9):
    num = int(input())
    if max < num:
        max = num
        count = i + 1
print(f'{max}\n{count}')
        