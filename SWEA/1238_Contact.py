# 데크로 풀기
from collections import deque

for tc in range(10):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 딕셔너리를 이용해서 자료 구조화
    graph = dict()

    # 입력받은 값을 순회하며 딕셔너리에 키:밸류 값으로 저장
    for i in range(0, len(arr), 2):
        if arr[i] not in graph:     # 해당 숫자가 없다면 딕셔너리에 새로운 키값 생성
            graph[arr[i]] = [arr[i + 1]]
        else:                       # 이미 숫자가 키값으로 존재한다면 밸류값에 추가
            graph[arr[i]].append(arr[i + 1])

    call_list = deque([start])  # 전화해야하는 노드가 담긴 큐
    called = []                 # 이미 전화한 노드에 또 전화하지 않기 위한 리스트
    rings = []                  # 언제 누구에게 전화되었는지 기록

    time = 0                    # 큐가 한 바퀴 돌때마다 시간 +1

    # BFS
    while call_list:
        for j in range(len(call_list)):
            now = call_list.popleft()
            if now not in called:
                called.append(now)
                rings.append((now, time))          # 노드, 시간 튜플로 기록
                if now in graph:
                    call_list.extend(graph[now])   # 전화해야하는 명단을 큐에 추가
        time += 1

    # 전화 기록 중 시간이 가장 크고, 숫자가 큰 값을 출력
    print(f'#{tc + 1} {max(rings, key=lambda x: (x[1], x[0]))[0]}')
