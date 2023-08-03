import sys

def ranking(award):
    rank = [0] * N
    now_rank = 0
    now_score = 3001
    for i in range(N):
        if award[i][1] < now_score:
            now_score = award[i][1]
            now_rank = i + 1
        rank[award[i][0]] = now_rank
    print(' '.join(map(str, rank)))

N = int(input())
awards = [{}, {}, {}, {}]

for i in range(3):
    row = list(map(int, input().split()))
    for j in range(N):
        awards[i][j] = row[j]
        if not i:
            awards[3][j] = row[j]
        else:
            awards[3][j] += row[j]

for i in range(4):
    ranking(sorted(awards[i].items(), key=lambda x: -x[1]))