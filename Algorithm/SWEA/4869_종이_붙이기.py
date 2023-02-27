def comb(n, m):   # 조합
    def fact(x):   # 팩토리얼
        if x == 1 or x == 0:
            return 1
        else:
            f = x * fact(x - 1)
        return f
    c = fact(n) // (fact(n - m) * fact(m))
    return c


for tc in range(int(input())):
    N = int(input()) // 10   # 나누기10해서 숫자 단순하게 입력
    ans = 0

    for i in range((N // 2) + 1):   # N 안에 가로길이 20짜리 종이가 들어가는 갯수만큼 반복
        if i == 0:   # 가로길이 20짜리 종이가 0개 들어가는 경우는 1가지
            ans += 1
        else:
            ans += comb(N - i, i) * (2 ** i)   # 가로길이 20짜리 종이가 들어가는 갯수의 조합 경우의 수와 가로 20짜리를 채우는 경우의 수의 곱

            # ㅁㅁㅁㅁㅁ N = 5일 경우
            # 1 1 1 1 1  가로길이가 10인 경우 1가지
            #  2  1 1 1
            # 1  2  1 1
            # 1 1  2  1
            #  1 1 1  2  20짜리가 1개 들어가는 경우 4(4C1) * 20짜리의 경우의 수 2 = 8
            #  2   2  1
            #  2  1  2
            # 1   2  2   20짜리가 2개 들어가는 경우 3(3C2) * 20짜리의 경우의 수 2^2 = 12

    print(f'#{tc + 1} {ans}')
