for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최소힙을 저장할 트리 리스트 초기화
    tree = [0]

    # 최소힙 구하기
    for i in arr:
        tree.append(i)

        child = len(tree) - 1
        parent = child // 2

        while parent and tree[child] < tree[parent]:
            tree[child], tree[parent] = tree[parent], tree[child]

            child = parent
            parent = child // 2

    # 정답 변수 초기화
    ans = 0

    # 마지막 노드의 바로 위 부모 노드 번호를 변수에 저장
    parent = (len(tree) - 1) // 2

    # 상위 부모 노드 값을 모두 정답 변수에 더하기
    while parent:
        ans += tree[parent]
        parent = parent // 2

    print(f'#{tc + 1} {ans}')
