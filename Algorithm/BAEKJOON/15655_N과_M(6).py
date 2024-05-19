def pick(depth=0, ans=[]):
    if depth > N:
        return
    if depth == N and len(ans) == M:
        print(*ans)
        return
    for n in range(depth, N):
        now = nums[n]
        if (now not in appended):
            appended.add(now)
            ans.append(now)
            pick(depth + 1, ans)
            ans.pop()
            pick(depth + 1, ans)
            appended.remove(now)

N, M = map(int, input().split())
ans_list = []
appended = set()
nums = sorted(list(map(int, input().split())))
pick()