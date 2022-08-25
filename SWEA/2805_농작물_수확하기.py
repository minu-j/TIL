for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N // 2):                 # 농장 크기를 2로 나눈 몫 만큼 반복,
        for j in range(N // 2, i, -1):      # 농장 크기를 2로 나눈 몫 만큼 반복하며 1씩 줄어드는 반복문
            matrix[i].pop()             # 우상단 값을 팝
            matrix[i].pop(0)            # 좌상단 값을 팝
            matrix[N - i - 1].pop()     # 우하단 값을 팝
            matrix[N - i - 1].pop(0)    # 좌하단 값을 팝

    ans = 0

    for i in matrix:   # 남아있는 값을 모두 더해서 정답 변수에 할당하기
        ans += sum(i)

    print(f'#{tc + 1} {ans}')