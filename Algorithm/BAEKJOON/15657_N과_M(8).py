def pick(depth=0, ans=[]):
    if len(ans) == M:
        print(*ans)
        return
    for n in range(depth, N):
        now = nums[n]
        ans.append(now)
        pick(n, ans)
        ans.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
pick()