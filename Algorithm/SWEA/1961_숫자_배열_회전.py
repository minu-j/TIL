for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 각 회전별 리스트, 정답을 저장할 리스트 생성
    r_90 = [[] for _ in range(N)]
    r_180 = [[] for _ in range(N)]
    r_270 = [[] for _ in range(N)]
    ans = [[] for _ in range(N)]

    count = 0

    # 90도로 세번 회전할때마다 각 각도별 리스트 변수와 정답 리스트에 저장
    for i in range(3):
        count += 1
        for x in range(N):
            for y in range(N - 1, -1, -1):
                if count == 1:
                    r_90[x].append(matrix[y][x])
                    ans[x].append(matrix[y][x])
                    continue
                elif count == 2:
                    r_180[x].append(r_90[y][x])
                    ans[x].append(r_90[y][x])
                    continue
                elif count == 3:
                    ans[x].append(r_180[y][x])
            ans[x].append('*')   # 정답의 각 숫자 사이에 *을 끼워넣어서 구분

    print(f'#{tc + 1}')
    for i in range(N):
        print(' '.join(''.join(map(str, ans[i])).split('*')))   # 정답 리스트를 *로 나눠서 join한 후 출력
