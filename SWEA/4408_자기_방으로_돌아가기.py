T = int(input())

for tc in range(T):
    N = int(input())

    while N > 0:
        last_room = 0

        for i in range(N):
            rooms = list(map(int, input().split())
            if rooms[0] > last_room:
