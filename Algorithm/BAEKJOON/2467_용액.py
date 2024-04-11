def bin_search(n, l, r):
    global ans

    c = (l + r) // 2
    diff = n + nums[c]

    if abs(diff) < ans[0]:
        ans = (abs(diff), n, nums[c])

    if l == r:
        return
    else:
        if diff < 0:
            bin_search(n, c + 1, r)
        elif 0 < diff:
            bin_search(n, l, c)
        else:
            ans = (abs(diff), n, nums[c])


N = int(input())
nums = list(map(int, input().split()))
ans = (9999999999, 0, 0)

for i in range(N - 1):
    bin_search(nums[i], i + 1, N - 1)

print(ans[1], ans[2])
