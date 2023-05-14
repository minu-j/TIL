from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    print_q = list(map(int, input().split()))
    imp_q = deque(sorted(print_q, reverse=True))
    cnt = 0
    while print_q[M] != 0:
        for idx in range(len(print_q)):
            if print_q[idx] == imp_q[0]:
                print_q[idx] = 0
                cnt += 1
                if idx == M:
                    break
                else:
                    imp_q.popleft()
    print(cnt)

