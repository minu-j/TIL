def pick(depth=0, ans=[]):
    if depth == M:
        print(*ans)
        return
    for n in range(N):
        now = nums[n]
        if (now not in appended):
            appended.add(now)
            ans.append(now)
            pick(depth + 1, ans)
            ans.pop()
            appended.remove(now)

N, M = map(int, input().split())
ans_list = []
appended = set()
nums = sorted(list(map(int, input().split())))
pick()