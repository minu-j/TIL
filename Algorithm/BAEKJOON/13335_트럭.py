from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)

t = 0

while True:
    bridge.popleft()

    now = trucks.popleft()
    if sum(bridge) + now <= L:
        bridge.append(now)
    else:
        bridge.append(0)
        trucks.appendleft(now)
    
    t += 1

    if len(trucks) == 0:
        break

print(t + w)