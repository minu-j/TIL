from collections import Counter

word = Counter(input().upper())
if len(word) == 1:
    exit(print(list(word.keys())[0]))
elif sorted(word.values())[-1] == sorted(word.values())[-2]:
    exit(print('?'))
else:
    exit(print(sorted(word.items(), key=lambda x: x[1])[-1][0]))
