from collections import deque

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]

    # 벽치기
    for i in maze:
        i.insert(0, 1)
        i.append(1)
    maze.insert(0, [1] * (N + 2))
    maze.append([1] * (N + 2))

    queue = deque()   # 데크로 큐 생성

    # 도착 위치 찾기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if maze[i][j] == 3:
                queue.append((i, j))
                break

    visited = []   # 방문 좌표 저장할 리스트 생성
    ans = 0
    count = 0

    flag = 1

    # bfs로 도착점에서 시작점 거꾸로 찾아가기
    while queue and flag:   # 큐가 비거나, 2를 찾아서 flag가 0이 되면 반복문 종료
        size = len(queue)

        # 큐 level이 같으면 중복으로 카운트되지 않도록 큐 사이즈만큼 반복하는 반복문
        for i in range(size):
            now = queue.popleft()
            if now not in visited:
                visited.append(now)

                # 델타검색을 위한 반복문
                for x, y in [0, 1], [1, 0], [0, -1], [-1, 0]:
                    if maze[now[0] + x][now[1] + y] == 2:   # 2랑 스치기만 해도 break
                        ans = count
                        flag = 0
                        break

                    # 해당 좌표가 반복된 적이 없고, 좌표의 값이 0이라면 큐에 추가
                    elif (now[0] + x, now[1] + y) not in visited and maze[now[0] + x][now[1] + y] == 0:
                        queue.append((now[0] + x, now[1] + y))
            if flag == 0:   # 2를 찾으면 반복문 탈출
                break

        count += 1

    print(f'#{tc + 1} {ans}')
