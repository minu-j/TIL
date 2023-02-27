N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
e = 0
count = 0
for i in range(N):
    if arr[i][0] >= e:
        e = arr[i][1]
        count += 1
print(count)