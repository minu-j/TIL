# def powerset(word, depth, n):
#     if depth == len(word):
#         if n == 1:
#             word1_set.add(''.join(select))
#         elif n == 2:
#             word2_set.add(''.join(select))
#         return
#
#     powerset(word, depth + 1, n)
#     select.append(word[depth])
#     powerset(word, depth + 1, n)
#     select.pop()
#
#
# word1 = input()
# word1_set = set()
# word2 = input()
# word2_set = set()
#
# select = []
# powerset(word1, 0, 1)
# powerset(word2, 0, 2)
#
# print(max(map(lambda x: len(x), word1_set & word2_set)))

from pprint import pprint

word1 = input()
word2 = input()

LCS = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

for i in range(1, len(word2) + 1):
    cnt = 0
    for j in range(1, len(word1) + 1):
        if cnt < LCS[i - 1][j - 1]:
            cnt = LCS[i - 1][j - 1]
        if word2[i - 1] == word1[j - 1]:
            LCS[i][j] = cnt + 1

    if i + 1 < len(word2) + 1:
        LCS[i + 1] = LCS[i][:]

print(max(LCS[-1]))