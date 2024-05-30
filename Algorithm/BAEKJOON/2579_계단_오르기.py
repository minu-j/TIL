N = int(input())
nums, dp = [0, 0, 0] + [int(input()) for _ in range(N)], [0] * (N + 3)

for i in range(3, N + 3):
    dp[i] = max(nums[i] + nums[i - 1] + dp[i - 3], nums[i] + dp[i - 2])

print(dp[-1])