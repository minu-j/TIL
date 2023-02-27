import sys
import heapq
input = sys.stdin.readline

hq = []
heapq.heapify(hq)

for n in range(int(input())):
    now = int(input())
    if now > 0:
        heapq.heappush(hq, (now, 1))
    elif now < 0:
        heapq.heappush(hq, (-now, -1))
    else:
        if hq:
            pop_now = heapq.heappop(hq)
            if pop_now[1] == 1:
                print(pop_now[0])
            else:
                print(-pop_now[0])
        else:
            print(0)
