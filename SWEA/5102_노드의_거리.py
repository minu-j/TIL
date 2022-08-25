from collections import deque

for tc in range(int(input())):
    V, E = map(int, input().split())
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        N_start, N_end = map(int, input().split())
        matrix[N_start][N_end] = 1
        matrix[N_end][N_start] = 1

    S, G = map(int, input().split())

    queue = deque()     # 데크로 큐를 생성
    queue.append(S)     # 시작점을 큐에 추가
    visited = []        # 방문 기록용 리스트
    ans = 0             # 정답을 저장할 변수
    count = 0           # 단계를 몇번 지나가는지 카운트하는 변수

    # BFS
    while queue:                        # 큐가 빌 때 까지 반복
        for i in range(len(queue)):     # 한 단계의 노드들을 한번의 카운트로 하기 위해 큐의 길이만큼 반복
            now = queue.popleft()
            if now not in visited:
                visited.append(now)
                for idx, j in enumerate(matrix[now]):
                    if j:
                        queue.append(idx)
        if G in queue:      # 도착점이 큐에 들어가면 카운트를 정답에 할당한 후 반복문 종료
            ans = count + 1     # 만약 도착점이 한번도 큐에 포함되지 않았으면 ans는 0이 될 것임.
            break
        count += 1

    print(f'#{tc + 1} {ans}')