direction = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


def signal(t, n, x, y, c, p):
    a = b = False
    count = 0
    if abs(x - position_A[1]) + abs(y - position_A[0]) <= c:
        a = True
        count += 1
    if abs(x - position_B[1]) + abs(y - position_B[0]) <= c:
        b = True
        count += 1
    return count, p, a, b


for tc in range(int(input())):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    BC = [tuple(map(int, input().split())) for _ in range(A)]
    MAP = [[0] * 10 for _ in range(10)]
    position_A, position_B = [1, 1], [10, 10]

    timeline = [[0] * (M + 1) for _ in range(2)]

    # print(timeline)

    # 20 시간 단위동안 진행
    for time in range(M + 1):
        # print('time =', time)
        # print('A', position_A, 'B', position_B)

        signal_AP = []

        for idx, bc in enumerate(BC):
            signal_AP.append(signal(time, idx, *bc))
        signal_AP.sort(key=lambda x: (x[0], x[1]))



        for N, power, is_A, is_B in signal_AP:
            if not N:
                continue
            elif N == 1:
                print(N, power, timeline[0][time], timeline[1][time])
                if is_A:
                    timeline[0][time] = power
                    print('A charging')
                else:
                    timeline[1][time] = power
                    print('B charging')
            else:
                print(N, power, timeline[0][time], timeline[1][time])
                # 둘다 0인 경우
                if not timeline[0][time] and not timeline[1][time]:
                    timeline[0][time] = timeline[1][time] = power // 2
                    print('A and B charging')
                else:
                    if power > timeline[0][time] and timeline[1][time] >= timeline[0][time]:
                        print('A charging')
                        timeline[0][time] = power
                    elif power > timeline[1][time] and timeline[0][time] > timeline[1][time]:
                        print('B charging')
                        timeline[1][time] = power

        # 시간이 지나면 A, B 위치 이동
        if time >= M:
            break
        position_A[0] += direction[move_A[time]][0]
        position_A[1] += direction[move_A[time]][1]
        position_B[0] += direction[move_B[time]][0]
        position_B[1] += direction[move_B[time]][1]

    print(*timeline, sep='\n')

    ans = 0

    print(f'#{tc + 1} {sum(timeline[0]) + sum(timeline[1])}')
