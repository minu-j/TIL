# 후위순회 순서의 트리 리스트를 생성하는 함수
def postorder(n):
    if left[n]:
        postorder(left[n])
    if right[n]:
        postorder(right[n])
    ordered_tree.append(tree[n])


for tc in range(10):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 노드의 값, 좌/우 노드 정보를 리스트에 입력
    for _ in range(N):
        input_list = list(input().split())
        if len(input_list) == 4:
            idx = int(input_list[0])
            tree[idx] = input_list[1]
            left[idx] = int(input_list[2])
            right[idx] = int(input_list[3])
        else:
            idx = int(input_list[0])
            tree[idx] = int(input_list[1])

    # 입력받은 트리 리스트를 후위순회 순서로 정렬
    ordered_tree = []
    postorder(1)

    # 후위연산
    stack = []
    for i in ordered_tree:
        if i == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A + B)
        elif i == '-':
            B = stack.pop()
            A = stack.pop()
            stack.append(A - B)
        elif i == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A * B)
        elif i == '/':
            B = stack.pop()
            A = stack.pop()
            stack.append(A / B)
        else:
            stack.append(i)

    print(f'#{tc + 1} {int(stack[0])}')
