T = int(input())

for tc in range(T):
    N = int(input())

    paper = [[0] * 10 for _ in range(10)]   # 10 * 10 격자 종이

    count = 0   # 보라색을 셀 변수

    for _ in range(N):   # 칠하는 횟수만큼 반복
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(10):   # 격자 종이를 순회하는 2중 for문
            for j in range(10):
                if r1 <= j <= r2 and c1 <= i <= c2:   # 해당 좌표가 칠하는 범위에 속하면
                    paper[i][j] += 1   # 좌표에 1 더하기
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 2:   # 만약 좌표값이 2면 두번 칠했다는 뜻이므로
                count += 1   # 보라색 +1

    print(f'#{tc + 1} {count}')