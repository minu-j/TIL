# 스도쿠 검증

def test(t):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if sorted(t) == a:
        return True
    # count = 0
    # for _ in range(8):
    #     if t[_] + 1 == t[_ + 1]:
    #         count += 1
    # if count == 8:
    #     return True


T = int(input())

for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    count_h = count_v = count_box = 0

    for i in range(9):
        # 가로 9줄 테스트
        if test(arr[i]) is True:
            count_h += 1

        # 세로 9줄 테스트
        test_v = []

        for j in range(9):
            test_v.append(arr[j][i])
        if test(test_v) is True:
            count_v += 1

    # 3X3 격자 테스트
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            test_box = []
            for x in range(3):
                for y in range(3):
                    test_box.append(arr[i + x][j + y])
            if test(test_box) is True:
                count_box += 1

    if count_h == 9 and count_v == 9 and count_box == 9:
        print(f'#{tc + 1} 1')
    else:
        print(f'#{tc + 1} 0')