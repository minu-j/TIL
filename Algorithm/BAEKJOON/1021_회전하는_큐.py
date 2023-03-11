N, M = map(int, input().split())
num_list = list(range(1, N + 1))
target_list = list(map(int, input().split()))
ans = 0

for target in target_list:
    target_idx = num_list.index(target)
    ans += min([target_idx, len(num_list) - target_idx])
    num_list = num_list[target_idx:] + num_list[:target_idx]
    num_list.pop(0)
print(ans)