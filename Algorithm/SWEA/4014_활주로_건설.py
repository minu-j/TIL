def check_runway(runway):
    global check

    for r in range(N - 1):
        if runway[r] - 1 > runway[r + 1]:
            return False   # 지형의 높이 차가 2 이상인 경우 False
        elif runway[r] - 1 == runway[r + 1]:
            for length in range(r + 1, r + 1 + X):
                if length >= N or runway[r + 1] != runway[length]:
                    return False   # 비탈길이 지형을 벗어나거나, 비탈길 길이 내 높이가 다른 지형이 있을 경우 False
                elif length < N:
                    check[length] += 1
                    if check[length] > 1:
                        return False   # 동일 지형에 비탈길이 겹쳐질 경우 False
    return True   # 나머지 경우는 True


for tc in range(int(input())):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    V_runway = [[] for _ in range(N)]
    H_runway = []

    for i in range(N):
        H_runway.append(matrix[i])
        for j in range(N):
            V_runway[i].append(matrix[j][i])

    for n in range(N):
        check = [0] * N   # 비탈길이 놓여지는 곳 체크
        if check_runway(V_runway[n]):   # 세로 활주로 순회하며 확인
            check = check[::-1]
            if check_runway(V_runway[n][::-1]):   # 세로 활주로를 뒤집어서 확인
                ans += 1   # 두가지 경우 다 건설 가능하다면 정답 +1

        check = [0] * N
        if check_runway(H_runway[n]):
            check = check[::-1]
            if check_runway(H_runway[n][::-1]):
                ans += 1

    print(f'#{tc + 1} {ans}')
