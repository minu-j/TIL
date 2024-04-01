from itertools import combinations

heights = [int(input()) for _ in range(9)]
for comb in list(combinations(heights, 7)):
    sum_comb = sum(comb)
    if sum_comb == 100:
        for height in sorted(comb):
            print(height)
        exit(0)
