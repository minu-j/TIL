from itertools import combinations_with_replacement
N, M = map(int, input().split())
for comb in list(combinations_with_replacement(list(range(1, N + 1)), M)):
    print(' '.join(map(str, comb)))