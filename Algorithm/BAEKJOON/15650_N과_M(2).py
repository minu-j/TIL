# from itertools import combinations

# N, M = map(int, input().split())
# for nums in list(combinations(list(range(1, N + 1)), M)): print(*nums)

def comb(depth=0, nums=[]):
    if depth == N and len(nums) == M:
        print(*nums)
        return
    for n in range(depth + 1, N + 1):
        if n not in appended:
            nums.append(n)
            appended.add(n)
            comb(depth + 1, nums)
            nums.pop()
            comb(depth + 1, nums)
            appended.remove(n)

N, M = map(int, input().split())
appended = set()
comb()