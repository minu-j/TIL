# from itertools import permutations

# N, M = map(int, input().split())
# for nums in list(permutations(range(1, N + 1), M)): print(*nums)

def perm(depth=0, nums=[]):
    if depth == M:
        print(*nums)
        return
    for n in range(1, N + 1):
        if n not in appended:
            nums.append(n)
            appended.add(n)
            perm(depth + 1, nums)
            nums.pop()
            appended.remove(n)

N, M = map(int, input().split())
appended = set()
perm()