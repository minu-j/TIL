sum_num = 1
while sum_num != 0:
    sum_num = sum(map(int, input().split()))
    if sum_num == 0:
        break
    else:
        print(sum_num)

# a = b = 0
# while True:
#     a, b = map(int, input().split())
#     if a and b != 0:
#         print(a + b)
#     else:
#         break