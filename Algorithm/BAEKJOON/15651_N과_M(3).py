def get_all_subset(depth=0, nums=[]):
    if depth == M:
        print(*nums)
        return
    for n in range(1, N + 1):
        nums.append(n)
        get_all_subset(depth + 1, nums)
        nums.pop()

N, M = map(int, input().split())
get_all_subset()