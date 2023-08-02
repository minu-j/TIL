# from collections import deque

# N, K = map(int, input().split())
# if N == K:
#     print(0)
#     exit(0)
# visited = {N: 0}

# Q = deque([(N, 0)])
# ans = 9999999999999999

# while Q:
#     for q in range(len(Q)):
#         X, T = Q.popleft()

#         # X - 1로 이동 하는 경우
#         if X - 1 == K:
#             if T + 1 < ans:
#                 ans = T + 1
#         elif 0 <= X - 1 <= 100_000:
#             # 이전에 X - 1을 방문한 적이 있다면
#             if X - 1 in visited:
#                 if visited[X - 1] > T + 1:
#                     visited[X - 1] = T + 1  # visited 시간 갱신
#                     Q.append((X - 1, T + 1))  # Q에 추가
#             # 방문한 적이 없다면
#             else:
#                 visited[X - 1] = T + 1      # visited 에 추가
#                 Q.append((X - 1, T + 1))    # Q에 추가

#         # X + 1로 이동 하는 경우
#         if X + 1 == K:
#             if T + 1 < ans:
#                 ans = T + 1
#         elif 0 <= X + 1 <= 100_000:
#             # 이전에 X - 1을 방문한 적이 있다면
#             if X + 1 in visited:
#                 if visited[X + 1] > T + 1:
#                     visited[X + 1] = T + 1  # visited 시간 갱신
#                     Q.append((X + 1, T + 1))  # Q에 추가
#             # 방문한 적이 없다면
#             else:
#                 visited[X + 1] = T + 1      # visited 에 추가
#                 Q.append((X + 1, T + 1))    # Q에 추가
#         # 2 * X로 이동 하는 경우
#         if 2 * X == K:
#             if T < ans:
#                 ans = T
#         elif 0 <= 2 * X <= 100_000:
#             # 이전에 X - 1을 방문한 적이 있다면
#             if 2 * X in visited:
#                 if visited[2 * X] > T:
#                     visited[2 * X] = T  # visited 시간 갱신
#                     Q.append((2 * X, T))  # Q에 추가
#             # 방문한 적이 없다면
#             else:
#                 visited[2 * X] = T      # visited 에 추가
#                 Q.append((2 * X, T))    # Q에 추가

# print(ans)

###########################################################

# # 8. 2. 0-1 BFS를 이용한 풀이

from collections import deque

LIMIT = 10**5 + 1
N, K = map(int, input().split())
visited = [9999999999] * LIMIT
q = deque([(N, 0)])
while q:
    for _ in range(len(q)):
        x, t = q.popleft()
        if x == K:
            print(t)
            exit(0)
        if 0 <= x - 1 < LIMIT and t + 1 < visited[x - 1]:
            visited[x - 1] = t + 1
            q.append((x - 1, t + 1))
        if 0 <= x + 1 < LIMIT and t + 1 < visited[x + 1]:
            visited[x + 1] = t + 1
            q.append((x + 1, t + 1))
        if 0 <= 2 * x < LIMIT and t < visited[2 * x]:
            visited[2 * x] = t
            q.appendleft((2 * x, t))
