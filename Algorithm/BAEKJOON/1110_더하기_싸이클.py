n = int(input())
original_n = n * 1
count = 0

while True:
    if 99 > n > 0:
        j = n % 10
        n = (n // 10) + (n % 10)
        n = (j * 10) + (n % 10)
        count += 1
        if n == original_n: break 
print(count)