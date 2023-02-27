for tc in range(10):
    T, E = map(int, input().split())
    way = list(map(int, input().split()))
    adj_matrix = [[0] * 100 for _ in range(100)]
    for i in range(0, (E * 2), 2):   # 입력받는게 어려웠습니다..
        adj_matrix[way[i]][way[i + 1]] += 1

    stack = [0]
    visit = []

    ans = 0

    while stack:   # dfs로 찾기
        current = stack.pop()
        if adj_matrix[current] not in visit:
            visit.append(current)
        for i in range(len(adj_matrix)):
            if adj_matrix[current][i] == 1:
                if i == 99:
                    stack.clear()
                    ans = 1
                    break
                stack.append(i)

    print(f'#{T} {ans}')