from collections import deque


# 각 사람이 어떤 계단으로 갈지 조합
def select_stairs(depth):
    if depth >= P:
        time_to_selected_stairs = [0] * P   # 각 사람이 선택한 계단까지의 거리를 담은 리스트
        for idx, s in enumerate(sel):
            if s:
                time_to_selected_stairs[idx] = time_to_stairs[idx][1]   # 1번계단으로 갈꺼면 1번계단까지 거리
            else:
                time_to_selected_stairs[idx] = time_to_stairs[idx][0]   # 0번계단으로 갈꺼면 0번계단까지 거리

        move(0, sel, time_to_selected_stairs, deque(), deque(), deque(), deque(), 0)   # 한번 움직여보기
        return

    for num in range(2):
        sel[depth] = num
        select_stairs(depth + 1)


# 선택한 계단에 따라 내려가는 시뮬레이션
def move(t, stair_num, left_time_to_stairs, down_s0, down_s1, wait_s0q, wait_s1q, down):
    global ans

    # 일단 계단 대기줄 먼저 교통정리하기
    # 지금 0번계단을 이용해 내려가고 있는 사람이 있는경우
    if down_s0:
        for _ in range(len(down_s0)):   # 각 사람별로 1씩 남은시간을 빼주고, 0이 아니면 다시 넣어주기
            now = down_s0.popleft()
            now -= 1
            if now > 0:
                down_s0.append(now)
            else:
                down += 1   # 남은시간이 0이 되면 1층에 도착했으므로 계단에서 꺼내고 내려간 사람 1 더하기

    # 0번 계단을 기다리는 사람이 있는 경우
    if wait_s0q:
        for _ in range(len(wait_s0q)):
            if len(down_s0) < 3:   # 계단에 3명 미만이 있으면?
                down_s0.append(wait_s0q.popleft())   # 대기줄에서 한명 꺼내서 계단에 넣기

    # 1번 계단도 동일하게 처리
    if down_s1:
        for _ in range(len(down_s1)):
            now = down_s1.popleft()
            now -= 1
            if now > 0:
                down_s1.append(now)
            else:
                down += 1

    if wait_s1q:
        for _ in range(len(wait_s1q)):
            if len(down_s1) < 3:
                down_s1.append(wait_s1q.popleft())

    # 내려간 사람이 총 사람 숫자랑 같으면 모두 내려갔으므로 재귀함수 끝내기
    if down == P:
        if t + 1 < ans:
            ans = t + 1
        return

    # 모든 사람들이 1분에 한칸씩 계단과 가까워지기
    for p in range(P):
        left_time_to_stairs[p] -= 1

        # 누군가 계단 입구에 도착한 경우
        if left_time_to_stairs[p] == 0:

            # 도착한 계단이 0번 계단이면 0번 계단 대기줄에 넣기
            if stair_num[p] == 0:
                wait_s0q.append(stairs[0][0])

            # 도착한 계단이 1번 계단이면 1번 계단 대기줄에 넣기
            elif stair_num[p] == 1:
                wait_s1q.append(stairs[stair_num[p]][0])

    # 이동이 다 끝나면 시간 +1
    if t + 2 < ans:   # t + 2가 이미 나온 정답과 같아지면 더이상 구하는 의미가 없으므로 가지치기
        move(t + 1, stair_num, left_time_to_stairs, down_s0, down_s1, wait_s0q, wait_s1q, down)


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    people = []
    time_to_stairs = []
    stairs = []

    # 계단 위치와 길이 찾아서 리스트에 더하기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] and matrix[i][j] != 1:
                stairs.append((matrix[i][j], (i, j)))

    # 사람 찾고 각 계단과 거리 구하기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                time_to_stairs.append((abs(i - stairs[0][1][0]) + abs(j - stairs[0][1][1]), abs(i - stairs[1][1][0]) + abs(j - stairs[1][1][1])))
                people.append((i, j))

    P = len(people)   # 총 인원수 자주 쓰니까 변수 하나 만들어놓기
    sel = [0] * P
    ans = 9999999999999999999
    select_stairs(0)

    print(f'#{tc + 1} {ans}')
