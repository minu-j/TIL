from itertools import combinations
N, M = map(int, input().split())
for comb in list(combinations(list(range(1, N + 1)), M)):
    print(' '.join(map(str, comb)))