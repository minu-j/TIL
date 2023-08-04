import sys

N = int(input())
bus = list(map(int, input().split()))

ans = 0
for i in range(N - 2):
    count = 0
    for j in range(i + 1, N):
        if bus[j] < bus[i]:
            ans += count
        if bus[i] < bus[j]:
            count += 1
print(ans)
