from collections import deque

for tc in range(int(input())):
    queue = deque(map(int, list(input())))

    ans = 0    # 정답 횟수를 카운트할 변수
    save = 0   # 해당 값을 저장할 변수

    for i in range(len(queue)):     # 큐 길이만큼 반복하여
        now = queue.popleft()       # popleft후 현재 값 변수에 저장
        if now == save:             # 현재 값이 저장된 값과 같다면 바꿀 필요가 없으므로 그대로 진행
            continue
        else:                       # 다르다면 0 또는 1로 바꿔줘야 하므로
            save = now              # 현재 값을 저장하고
            ans += 1                # 정답 +1

    print(f'#{tc + 1} {ans}')
