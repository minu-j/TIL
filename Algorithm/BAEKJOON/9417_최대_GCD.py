from itertools import combinations
from math import gcd

for tc in range(int(input())):
    ans = 1
    for a, b in combinations(map(int, input().split()), 2):
        ans = max(gcd(a, b), ans)
    print(ans)
