n = int(input())

count = 1
a = n // 10
b = n % 10
mr = 0

while count < 10:
    if n < 10:
        n = n + mr * 10    
    else:
        a = n // 10
        b = n % 10 
        n = a + b
    count += 1
    print(n, count)