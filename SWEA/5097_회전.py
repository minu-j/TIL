# 데크로 풀기
# from collections import deque
#
# for tc in range(int(input())):
#     N, M = map(int, input().split())
#     queue = deque(map(int, input().split()))
#     for i in range(M):
#         now = queue.popleft()
#         queue.append(now)
#     print(f'#{tc + 1} {queue.popleft()}')

# 다른 풀이 -> M을 N으로 나눈 나머지의 위치와 동일
for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc + 1} {arr[M % N]}')
