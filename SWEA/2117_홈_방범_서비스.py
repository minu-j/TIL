# x, y를 기준으로 k 크기만큼 주어진 모양처럼 마을에 +1을 해주는 함수
def mark(y, x, mk):
    k_size = mk * 2 - 1
    y_point = y - mk + 1
    x_point = x - mk + 1
    for mi in range(k_size):
        for mj in range(k_size):
            if 0 <= y_point + mi < N and 0 <= x_point + mj < N:
                town[y_point + mi][x_point + mj] += 1
    for mi in range(mk - 1):
        for mj in range(mk - 2 - mi, -1, -1):
            if 0 <= y_point + mi < N and 0 <= x_point + mj < N:
                town[y_point + mi][x_point + mj] -= 1
            if 0 <= y_point + mi < N and 0 <= x_point + mk * 2 - 2 - mj < N:
                town[y_point + mi][x_point + mk * 2 - 2 - mj] -= 1
            if 0 <= y_point + mk * 2 - 2 - mi < N and 0 <= x_point + mj < N:
                town[y_point + mk * 2 - 2 - mi][x_point + mj] -= 1
            if 0 <= y_point + mk * 2 - 2 - mi < N and 0 <= x_point + mk * 2 - 2 - mj < N:
                town[y_point + mk * 2 - 2 - mi][x_point + mk * 2 - 2 - mj] -= 1


for tc in range(int(input())):
    N, M = map(int, input().split())
    town_original = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 정답이 전체 집 갯수랑 동일해져버리면 더이상 찾을 필요가 없음.
    house_max = 0
    for i in range(N):
        for j in range(N):
            if town_original[i][j] == 1:
                house_max += 1

    # 모든 경우의 수 다 구해버리기
    for i in range(N):
        for j in range(N):
            for k in range(N * 2):
                town = []
                for row in town_original:
                    town.append(row[::])
                mark(i, j, k)
                cost = (k * k + (k - 1) * (k - 1))
                house = 0
                for row in town:
                    house += row.count(2)
                income = (house * M) - cost

                if income >= 0 and house > ans:
                    ans = house
                if ans == house_max:   # 정답이 최대 갯수에 도달하면 반복문 종료
                    break
            if ans == house_max:
                break
        if ans == house_max:
            break

    print(f'#{tc + 1} {ans}')
