def test(t1, t2):
    S = score
    A = 0
    B = 0
    C = 0
    for idx_s in range(len(S)):
        if t2 <= idx_s:
            # print('A', S[idx_s])
            A += S[idx_s]
        elif t1 <= idx_s < t2:
            # print('B', S[idx_s])
            B += S[idx_s]
        elif idx_s < t1:
            # print('C', S[idx_s])
            C += S[idx_s]

    if K_min <= A <= K_max and K_min <= B <= K_max and K_min <= C <= K_max:
        # print('True', A, B, C, t1, t2)

        return max(A, B, C) - min(A, B, C)
    else:
        # print('False', A, B, C, t1, t2)
        return False


for tc in range(int(input())):
    N, K_min, K_max = map(int, input().split())
    imp = list(map(int, input().split()))

    score = [0] * 101

    for idx, i in enumerate(imp):
        score[i] += 1

    ans = 999999999999999

    # print(test(3, 5))

    for T1 in range(1, 101):
        for T2 in range(T1, 101):
            T = test(T1, T2)
            # print(T)
            if T is False:
                continue
            else:
                if T < ans:
                    ans = T

    if ans == 999999999999999:
        ans = -1



    print(f'#{tc + 1} {ans}')
