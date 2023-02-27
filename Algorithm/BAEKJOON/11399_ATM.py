N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += arr[-i + -1] * (i + 1)
print(ans)