from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0

pick = list(map(sum, combinations(cards, 3)))
for p in pick:
    if ans < p <= M:
        ans = p

print(ans)