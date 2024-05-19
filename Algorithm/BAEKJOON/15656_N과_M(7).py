def pick(depth=0, ans=[]):
    if depth == M:
        print(*ans)
        return
    for n in range(N):
        now = nums[n]
        ans.append(now)
        pick(depth + 1, ans)
        ans.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
pick()