from itertools import combinations
from collections import deque

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

matrix = []
som = set()

for i in range(5):
    row = input()
    for j in range(5):
        matrix.append((i, j))
        if row[j] == 'S':
            som.add((i, j))

combs = combinations(matrix, 7)
ans = 0

for comb in combs:
    start = comb[0]
    comb_set = set(comb)
    comb_set.remove(start)
    
    q = deque([start])
    count = 0
    count_som = 0
    while q:
        i, j = q.popleft()
        if (i, j) in som:
                    count_som += 1
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if (ni, nj) in comb_set:
                count += 1
                comb_set.remove((ni, nj))
                q.append((ni, nj))
    if count == 6 and count_som >= 4:
        ans += 1
print(ans)