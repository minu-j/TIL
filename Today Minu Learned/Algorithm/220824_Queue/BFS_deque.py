from collections import deque

point, line = map(int, input().split())
way = list(map(int, input().split()))

# 인접행렬에 경로 값 추가
matrix = [[0] * (point + 1) for _ in range(point + 1)]
for i in range(0, len(way), 2):
    matrix[way[i]][way[i + 1]] = 1
    matrix[way[i + 1]][way[i]] = 1

# 큐와 방문했던 노드를 기록할 리스트 추가
queue = [1]
visit = []

# 큐가 비어있지 않는 동안 반복
while queue:
    now = queue.pop(0)              # 현재 위치는 큐의 가장 앞
    if now not in visit:            # 만약 현재위치가 방문되지 않았다면?
        print(now, end=' ')         # 현재 위치를 출력한 후
        visit.append(now)           # 방문 리스트에 현재 위치를 추가하여 다음번에 다시 방문하지 않도록 함.
        for i in range(len(matrix[now])):   # 현재 위치와 연결되어있는 노드를 확인해서
            if matrix[now][i]:              # 노드가 연결되어 있다면
                queue.append(i)             # 큐에 추가해준다.
