T = int(input())
nums = [int(input()) for _ in range(T)]
dp = [0] * 1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, max(nums) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for n in nums:
    print(dp[n])
