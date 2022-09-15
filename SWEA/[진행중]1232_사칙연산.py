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

    stack = []

    for j in order:
        stack.append(tree[0][j])

    print(tree)
    print(order)
    print(stack)

    nums = []
    for k in stack:
        print(k, nums)
        if k == "+":
            B = nums.pop()
            A = nums.pop()
            nums.append(A + B)
        elif k == "-":
            B = nums.pop()
            A = nums.pop()
            nums.append(A - B)
        elif k == "*":
            B = nums.pop()
            A = nums.pop()
            nums.append(A * B)
        elif k == "/":
            B = nums.pop()
            A = nums.pop()
            nums.append(A / B)
        else:
            nums.append(int(k))

    print(f'#{tc + 1} {int(nums[-1])}')
