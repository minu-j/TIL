from collections import defaultdict
input()
cnt_dict = defaultdict(int)
for n in list(map(int, input().split())):
    cnt_dict[n] += 1
input()
print(' '.join([str(cnt_dict[m]) for m in list(map(int, input().split()))]))
