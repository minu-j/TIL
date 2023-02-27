for tc in range(int(input())):
    V, E = map(int, input().split())                        # 노드와 경로의 갯수를 입력받아서
    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]      # 경로 매트릭스 작성
    for e in range(E):                                      # 경로의 갯수만큼 반복하여 경로를 입력받는데,
        start, end = map(int, input().split())
        adj_matrix[start][end] += 1                         # 방향성 그래프이므로 일방향으로만 경로를 표시함
    S, G = map(int, input().split())
    ans = 0

    stack = [S]
    visit = []

    # DFS

    while stack:
        current = stack.pop()
        if current not in visit:
            visit.append(current)

        for i in range(len(adj_matrix[current])):
            if adj_matrix[current][i]:
                if i in visit:
                    continue
                elif i == G:        # 탐색하는 노드가 도착점에 닿는것만으로 탐색 종료
                    ans = 1
                    stack.clear()   # 스택을 비워서 while 종료
                    break
                else:
                    stack.append(i)

    print(f'#{tc + 1} {ans}')
