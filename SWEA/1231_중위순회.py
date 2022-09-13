# 중위순회
def inorder(n):
    if tree[1][n]:
        inorder(n * 2)
    print(tree[0][n], end='')
    if tree[2][n]:
        inorder(n * 2 + 1)


for tc in range(10):
    print(f'#{tc + 1}', end=' ')   # 테스트케이스 번호 출력
    N = int(input())
    tree = [[0] * (N + 1) for _ in range(3)]    # tree[0]은 글자, [1]은 왼쪽 자식노드, [2]는 오른쪽 자식노드
    for i in range(N):                          # 노드 갯수만큼 반복
        node_list = input().split()
        tree[0][int(node_list[0])] = node_list[1]
        if len(node_list) >= 3:                 # 입력받은 리스트가 3보다 길다면 왼쪽노드가 있다는 뜻임.
            tree[1][int(node_list[0])] = int(node_list[2])
        if len(node_list) >= 4:
            tree[2][int(node_list[0])] = int(node_list[3])

    inorder(1)
    print()