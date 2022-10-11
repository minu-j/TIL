def test(k, ab, depth, point, mtx, change_count, conv):
    global ans

    if change_count >= ans:
        return

    # 해당 컬럼이 pass 조건인지 먼저 확인해서, 조건에 맞을 경우 다음 컬럼으로 넘기기
    column_count = [1] * D
    count = 0
    key = 0
    column_pass = False
    for _ in range(D):
        if _ == 0:
            key = mtx[_][point]
        else:
            if key == mtx[_][point]:
                count += 1
                column_count[_] += count
                if column_count[_] >= k:
                    column_pass = True
                    break
            else:
                key = mtx[_][point]
                count = 0

    if column_pass:
        if point + 1 == W:
            # print('테스트 통과', change_count, point)
            if ans > change_count:
                ans = change_count
                return

        else:
            # print('다음 point 이동', pass_count, point)
            test(k, 2, 0, point + 1, mtx, change_count, conv)

    # 조건에 맞지 않으면 이리저리 바꿔볼 필요가 있음.
    else:
        if depth == 0:
            # 맨 윗줄은 안보고 패스
            test(k, mtx[0][point], depth + 1, point, mtx, change_count, conv)

        # 해당 속성과 윗 속성이 같은 경우
        elif mtx[depth][point] == ab:
            if depth + 1 == D:
                return
            elif depth + 1 < D:
                # 다음 줄로 이동
                test(k, ab, depth + 1, point, mtx, change_count, conv)

        # 해당 속성과 다음 속성이 다른 경우
        elif mtx[depth][point] != ab:

            # 해당 줄을 반대 용액으로 채워보기
            if not conv[depth]:
                memory = mtx[depth]
                mtx[depth] = [ab] * W
                conv[depth] = True
                test(k, 2, 0, 0, mtx, change_count + 1, conv)
                mtx[depth] = memory
                conv[depth] = False

            # 바로 전 줄을 반대의 용액으로 채워보기
            if not conv[depth - 1]:
                memory = mtx[depth - 1]
                mtx[depth - 1] = [mtx[depth][point]] * W
                conv[depth - 1] = True
                test(k, 2, 0, 0, mtx, change_count + 1, conv)
                mtx[depth - 1] = memory
                conv[depth - 1] = False

            # print('333 아님 그냥 넘겨')
            if depth + 1 == D:
                return
            elif depth + 1 < D:
                test(k, mtx[depth][point], depth + 1, point, mtx, change_count, conv)


for tc in range(int(input())):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]

    if K == 1:
        ans = 0
    else:
        converted = [False] * D
        ans = D
        test(K, 2, 0, 0, matrix, 0, converted)

    print(f'#{tc + 1} {ans}')
