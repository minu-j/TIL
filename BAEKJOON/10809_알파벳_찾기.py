from collections import Counter
count = Counter(map(chr, list(range(97, 123))))
for x in count:
    count[x] = -1
for index, y in enumerate(input()):
    if count[y] == -1:
        count[y] = index
print(*count.values())