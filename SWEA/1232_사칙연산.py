def inorder(n):
    if n > N:
        return
    inorder(n * 2)
    inorder(n * 2 + 1)
    order.append(n)


for tc in range(10):
    N = int(input())
    ans = 0

    tree = [[0] * (N + 1) for _ in range(3)]

    for i in range(N):
        case_list = list(input().split())

        if len(case_list) == 4:
            tree[0][int(case_list[0])] = case_list[1]
            tree[1][int(case_list[0])] = case_list[2]
            tree[2][int(case_list[0])] = case_list[3]
        else:
            tree[0][int(case_list[0])] = case_list[1]

    order = []
    inorder(1)

    queue = []

    for j in order:
        queue.append(tree[0][j])

    nums = []
    for k in queue:
        if k == "+":
            nums = [nums[0] + nums[1]]
        elif k == "-":
            nums = [nums[0] - nums[1]]
        elif k == "*":
            nums = [nums[0] * nums[1]]
        elif k == "/":
            nums = [nums[0] / nums[1]]
        else:
            nums.append(int(k))

    print(f'#{tc + 1} {nums[0]}')
