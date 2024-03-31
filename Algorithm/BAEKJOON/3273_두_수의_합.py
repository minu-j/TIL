n, nums, x = int(input()), sorted(
    list(map(int, input().split()))), int(input())
ans = 0
for i in range(n - 1):
    target = x - nums[i]
    for j in range(i + 1, n):
        if nums[j] == target:
            ans += 1
        elif nums[j] > target:
            break
print(ans)
