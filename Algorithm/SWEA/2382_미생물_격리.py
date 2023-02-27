from pprint import pprint

direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    micro = {}

    for k in range(K):
        Y, X, num, D = map(int, input().split())   # [ 세로위치, 가로위치, 미생물 수, 이동방향 ]
        micro[(Y, X)] = [(num, D)]   # micro[ 좌표 ] = [ 미생물 수, 이동방향 ]

    for m in range(M):   # 시간
        move_micro = {}
        for y, x in micro:
            n, d = micro[(y, x)][0]

            move_y, move_x = y + direction[d][0], x + direction[d][1]

            # 움직인 곳이 격리구역 안쪽일 경우
            if 0 < move_y < N - 1 and 0 < move_x < N - 1:

                # 이미 그 자리에 다른 미생물이 움직였을 경우
                if (move_y, move_x) in move_micro:
                    move_micro[(move_y, move_x)].append((n, d))

                # 아직 그 자리에 아무도 없을 경우.
                else:
                    move_micro[(move_y, move_x)] = [(n, d)]   # 미생물 수와 방향을 그대로 유지

            # 움직인 곳이 약품구역일 경우
            elif 0 == move_y or move_y == N - 1 or 0 == move_x or move_x == N - 1:
                n = n // 2
                if n == 0:
                    continue

                if d == 1:
                    move_micro[(move_y, move_x)] = [(n, 2)]
                elif d == 2:
                    move_micro[(move_y, move_x)] = [(n, 1)]
                elif d == 3:
                    move_micro[(move_y, move_x)] = [(n, 4)]
                elif d == 4:
                    move_micro[(move_y, move_x)] = [(n, 3)]

        # 겹친 미생물 병합하기
        for y, x in move_micro:
            z = sorted(move_micro[(y, x)], reverse=True)
            d = z[0][1]
            n = 0
            for _ in move_micro[(y, x)]:
                n += _[0]
            move_micro[(y, x)] = [(n, d)]

        micro = move_micro

    ans = 0
    for v in micro.values():
        ans += v[0][0]

    print(f'#{tc + 1} {ans}')
