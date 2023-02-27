for tc in range(int(input())):
    N, M, L = map(int, input().split())

    # 빈 리스트 만들기
    num_list = [0] * (N + 1)   # 해당 노드의 값
    left = [0] * (N + 1)       # 왼쪽 자식 노드
    right = [0] * (N + 1)      # 오른쪽 자식 노드

    # N 개의 노드를 갖는 완전 이진 트리 만들기
    for i in range(1, N // 2 + 1):
        if i * 2 <= N:
            left[i] = (i * 2)
        if i * 2 + 1 <= N:
            right[i] = (i * 2 + 1)

    # 리프 노드의 값 입력 받기
    for j in range(M):
        leaf, num = map(int, input().split())
        num_list[leaf] = num

    # 자식 노드로 부모 노드를 탐색하면서 두 자식노드 값의 합을 부모노드에 지정하기
    for k in range(N, 0, -1):
        if left[k]:
            num_list[k] = num_list[left[k]] + num_list[right[k]]

    ans = 0

    print(f'#{tc + 1} {num_list[L]}')
