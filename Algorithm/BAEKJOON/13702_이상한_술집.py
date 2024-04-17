def possible_separate(n):
    parts = 0
    for num in nums:
        if n:
            parts += (num // n)
    return True if K <= parts else False


N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

l, r = 1, max(nums)

ans = 0
while l <= r:
    m = (l + r) // 2
    if possible_separate(m):
        if ans < m:
            ans = m
        l = m + 1
    else:
        r = m - 1

print(ans)
