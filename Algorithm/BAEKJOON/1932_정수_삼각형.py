N = int(input())
dp = [0]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i + 1):
        if j == 0:
            row[j] = dp[j] + row[j]
        else:
            row[j] = max(dp[j - 1] + row[j], dp[j] + row[j])
    dp = row + [0]
print(max(dp))