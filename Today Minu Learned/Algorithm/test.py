a = [3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 9]

count = [0] * 11

for i in a:
    count[i] += 1

print(count)

sort_a = [0] * len(a)

for i in range(len(count)):
    count[i] = count[i] + count[i - 1]

print(count)

for i in range(len(a) - 1, -1, -1):
    sort_a[count[a[i]] - 1] = a[i]
    print(sort_a)
    count[a[i]] -= 1