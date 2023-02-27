for tc in range(int(input())):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 2차원 퍼즐 배열을 전치해서 두번 검사해야 하므로 2번 반복하는 반복문
    for i in range(2):

        # 퍼즐 안에 있는 K와 일치하는 1의 갯수를 세기 위한 반복문
        for j in range(N):
            line = ''.join(map(str, puzzle[j])).split('0')   # 해당 줄의 배열을 텍스트로 변환한다음, 0을 기준으로 나누기
            for k in line:          # 해당 줄의 길이만큼 순회하여
                if K == len(k):     # K와 해당 줄의 길이가 같다면
                    ans += 1        # 정답 +1

        # 가로를 한번 봤으면 세로를 봐야하므로 2차원 배열을 전치
        for j in range(N):
            for k in range(N):
                if j > k:
                    puzzle[j][k], puzzle[k][j] = puzzle[k][j], puzzle[j][k]

    print(f'#{tc + 1} {ans}')
