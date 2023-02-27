for tc in range(int(input())):
    N = int(input())
    ans = True

    # 학익진 코딩
    while ans:
        for a in range(24):
            for b in range(15):
                for c in range(11):
                    for d in range(9):
                        for e in range(7):
                            if (2 ** a) * (3 ** b) * (5 ** c) * (7 ** d) * (11 ** e) == N:   # 각 제곱의 곱이 N과 같으면 출력 후 break
                                print(f'#{tc + 1}', end=' ')
                                print(a, b, c, d, e)
                                ans = False
                                break
                        if ans is False:
                            break
                    if ans is False:
                        break
                if ans is False:
                    break
            if ans is False:
                break
