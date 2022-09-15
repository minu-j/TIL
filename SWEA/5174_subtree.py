# subtree의 노드 갯수를 세는 함수
def search_node(n):
    global ans
    ans += 1   # 노드에 한번 접근하면 정답 +1
    if tree[0][n]:   # 만약 리스트의 값이 0이 아니라면 자식노드가 있는 것이므로 그 아래 노드를 센다
        search_node(tree[0][n])
    if tree[1][n]:
        search_node(tree[1][n])


for tc in range(int(input())):
    E, N = map(int, input().split())
    tree = [[0] * (E + 2) for _ in range(2)]   # E + 2의 길이만큼 리스트 2개 생성
    arr = list(map(int, input().split()))

    # 트리 리스트에 간선 정보 입력
    for i in range(0, len(arr), 2):
        if tree[0][arr[i]]:   # 만약 해당 노드의 왼쪽 자식노드의 값이 있다면
            tree[1][arr[i]] = arr[i + 1]   # 오른쪽 노드로 입력
        else:
            tree[0][arr[i]] = arr[i + 1]

    ans = 0
    search_node(N)

    print(f'#{tc + 1} {ans}')
