def seq(n):
    return n * (n + 1) // 2


N = int(input())
arr = list(map(int, input().split()))

visited = set()
break_idx = set()
point = [0, 0]
prev = 0
ans = 0

for i in range(N):
    if arr[i] in visited:
        ans += seq(point[1] - point[0]) - seq(prev - point[0])
        break_idx.add(arr[i])
        while True:
            if arr[point[0]] in break_idx:
                point[0] += 1
                prev = point[1]
                break
            point[0] += 1
    else:
        visited.add(arr[i])
    point[1] += 1

ans += seq(point[1] - point[0]) - seq(prev - point[0])
print(ans)
