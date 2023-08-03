# import sys

# times = sorted([tuple(map(int, input().split())) for _ in range(int(sys.stdin.readline()))], key=lambda x: (x[1], -x[0]))
# ans = 0
# prev = 0
# for time in times:
#     if prev <= time[0]:
#         prev = time[1]
#         ans += 1
# print(ans)

# import sys

# N = int(input())
# times = {}
# for i in range(N):
#     s, f = map(int, input().split())
#     if f not in times:
#         times[f] = s
#     elif times[f] < s:
#         times[f] = s
# ans = 0
# prev = 0
# for f, s in sorted(times.items()):
#     if prev <= s:
#         prev = f
#         ans += 1
# print(ans)

from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
times = []

for i in range(N):
    s, f = map(int, input().split())
    heappush(times, (f, s))
ans = 0
prev = 0
while times:
    f, s = heappop(times)
    if prev <= s:
        prev = f
        ans += 1
print(ans)
