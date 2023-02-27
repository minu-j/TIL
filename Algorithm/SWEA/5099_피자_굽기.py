from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    pizza = deque(map(int, input().split()))
    oven = deque([(0, 0)] * N)   # 일단 오븐에 빈칸을 넣어줌
    idx = 1                      # 피자 번호를 체크할 인덱스

    # 오븐 돌리기
    while oven:                         # 오븐이 빌 때 까지 반복
        now = oven.popleft()            # 오븐 가장 왼쪽에 있는 피자를 꺼내서
        now = (now[0], now[1] // 2)     # 치즈를 반으로 줄이기
        if now[1] == 0:                                 # 만약 치즈가 0이 되면
            if pizza:
                oven.append((idx, pizza.popleft()))     # 남은 피자중에서 하나를 꺼내서 오븐에 넣고
                idx += 1                                # 피자 인덱스 카운트 +1
        else:
            oven.append(now)            # 치즈가 아직 남아있으면 피자 다시 집어넣기

    print(f'#{tc + 1} {now[0]}')