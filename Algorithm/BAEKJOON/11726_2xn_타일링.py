count = [1, 1]
now = 1
for i in range(9 - 1):
    now = count[0] + count[1]
    count[0] = count[1]
    count[1] = now
print(now % 10007)