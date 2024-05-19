def get_max_num(depth=0, nums=[], nums_sum=0):
    global ans
    if depth == N:
        if ans < nums_sum:
            ans = nums_sum
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        nums.append(inputs[i])
        get_max_num(depth + 1, nums, nums_sum + abs(nums[depth - 1] - inputs[i]))
        nums.pop()
        visited[i] = False

N, inputs =  int(input()), list(map(int, input().split()))
visited, ans = [False] * N, 0
get_max_num()
print(ans)