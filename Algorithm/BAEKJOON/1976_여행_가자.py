# N, M = [int(input()) for _ in range(2)]
# town_list = [set() for _ in range(201)]
# for i in range(N):
#     town = list(map(int, input().split()))
#     for j in range(N):
#         if town[j]:
#             start, end = i + 1, j + 1
#             town_list[start].add(end)
#             town_list[start] = town_list[end] = town_list[start] | town_list[end]
            
# route = list(map(int, input().split()))

# if M == 1 and route[0] not in town_list[route[0]]:
#     print("NO")
#     exit(0)
# else:
#     for idx in range(M - 1):
#         if route[idx + 1] not in town_list[route[idx]] and route[idx] != route[idx + 1]:
#             print("NO")
#             exit(0)
#         elif not town_list[route[idx]]:
#             print("NO")
#             exit(0)
# print("YES")

# # # input
# 3
# 2
# 0 1 0
# 1 0 0
# 0 0 0
# 3 3
# # # output
# # NO
# # # answer
# # YES

N, M = [int(input()) for _ in range(2)]
town_list = [{_} for _ in range(N + 1)]
for i in range(N):
    town = list(map(int, input().split()))
    for j in range(N):
        if town[j]:
            start, end = i + 1, j + 1
            town_list[start].add(end)
            town_list[start] = town_list[end] = town_list[start] | town_list[end]
            
route = list(map(int, input().split()))

for i in range(M - 1):
    if route[i + 1] not in town_list[route[i]]:
        print("NO")
        exit(0)
print("YES")

# # 9%에서 틀렸습니다
