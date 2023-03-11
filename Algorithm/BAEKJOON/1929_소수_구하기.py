import math

M, N = map(int, input().split())

for num in range(M, N + 1):
    PN = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            PN = False
            break
        i += 1
    if PN:
        print(num)
