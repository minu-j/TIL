from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
word_list = [input() for _ in range(N)]
ans = 0

for i in range(1, len(word_list) + 1):
    word_comb_list = (list(combinations(word_list, i)))
    for word_comb in word_comb_list:
        chr_set = set()
        for word in word_comb:
            chr_set = chr_set | set(word)
        if len(word_comb) > ans and len(chr_set) <= K:
            ans = len(word_comb)

print(ans)