for tc in range(10):
    T, maze = int(input()), [list(map(int, list(input()))) for _ in range(16)]

    stack = []
    visited = []
    ans = 0

    for i in range(16):   # 미로 내에서 시작점의 좌표를 튜플로 검색
        for j in range(16):
            if maze[i][j] == 2:
                stack = [(i, j)]   # 값이 2인 경우 시작점이므로 스택에 저장

    while stack:   # 스택이 True면 반복
        current = stack.pop()   # 스택의 맨 뒷 값을 팝
        if current not in visited:   # 해당 좌표가 방문되지 않았다면
            visited.append(current)   # 방문 기록에 좌표를 추가

        # 델타검색으로 좌표 순회하며 도착점 찾기
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for i in range(4):   # 델타검색의 네 방향대로 반복
            x = current[0] + di[i]
            y = current[1] + dj[i]

            if maze[x][y] == 3:   # 만약 좌표의 값이 3이면 도착점이므로
                ans = 1   # 정답은 1이며,
                break   # 즉시 탐색 종료

            elif maze[x][y] == 1 or maze[x][y] == 2:   # 좌표의 값이 1 또는 2이면 방문할 필요가 없으므로
                continue   # 무시

            elif (x, y) not in visited:   # 좌표 값이 1, 2, 3이 아니고, 방문한 기록이 없다면
                stack.append((x, y))   # 스택에 해당 좌표를 추가

    print(f'#{T} {ans}')
