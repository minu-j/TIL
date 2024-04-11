def get_jealousy(n):
    over_cnt = M
    for i in range(M):
        if nums[i] <= n:
            break
        over_cnt += (nums[i] - 1) // n
    return True if over_cnt <= N else False


N, M = map(int, input().split())
nums = sorted([int(input()) for _ in range(M)], reverse=True)

ans, l, m, r = nums[0], 1, nums[0] // 2, nums[0]
while l < r:
    if get_jealousy(m):
        if m < ans:
            ans = m
        r = m
    else:
        l = m + 1
    m = (l + r) // 2
print(ans)
