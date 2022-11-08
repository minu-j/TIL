import sys
import heapq
input = sys.stdin.readline

hq = []
heapq.heapify(hq)

for n in range(int(input())):
    now = -int(input())
    if not now:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, now)
