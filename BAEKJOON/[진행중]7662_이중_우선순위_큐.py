import sys
from heapq import *
input = sys.stdin.readline


def change(q):
    new_q = []
    for _ in q:
        heappush(new_q, -_)
    return new_q


for tc in range(int(input())):
    Q = []  # 큐 초기화
    status = -1

    for k in range(int(input())):
        C, n = input().split()

        if C == 'I':    # 삽입모드
            n = int(n)
            heappush(Q, n)

        elif C == 'D':  # 삭제모드
            if len(Q) > 0:      # Q가 비어있지 않을 때
                if n == '-1':     # n이 -1이라면 Q의 최솟값 삭제
                    if status == 1:
                        Q = change(Q)
                        status = -1
                    heappop(Q)
                elif n == '1':    # n이 1이라면 Q의 최댓값 삭제
                    if status == -1:
                        Q = change(Q)
                        status = 1
                    heappop(Q)

    if len(Q) == 0:
        print('EMPTY')
    else:
        print(max(Q), min(Q))
