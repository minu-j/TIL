for tc in range(int(input())):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = 'NO'

    # 델타 좌표 생성 [오른쪽, 우하향 대각선, 아래, 좌하향 대각선]
    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]

    # 2차원 배열을 순회하며 'o' 찾기
    for i in range(N):
        for j in range(N):

            # 해당 좌표가 'o'일 때 해당 좌표를 기점으로 오른쪽, 우하향 대각선, 아래, 좌하향 대각선을 확인해야 함.
            if board[i][j] == 'o':

                # 델타 좌표만큼 반복하며 카운트
                for k in range(4):
                    count = 0

                    # 앞으로 4개 돌을 더 보면서 오목인지 확인
                    for l in range(1, 5):

                        # 만약 가로, 세로 인덱스가 오목판의 범위를 넘지 않으면서
                        if 0 <= i + (di[k] * l) < N and 0 <= j + (dj[k] * l) < N:

                            # 그 다음 오목돌이 'o'일 경우 카운트+1
                            if board[i + (di[k] * l)][j + (dj[k] * l)] == 'o':
                                count += 1

                            # 아닐 경우 반복문 종료
                            else:
                                break

                    # 누적 카운트가 4면 오목이므로 정답 YES 후 반복문 종료
                    if count == 4:
                        ans = 'YES'
                        break
            if ans == 'YES':
                break
        if ans == 'YES':
            break

    print(f'#{tc + 1} {ans}')
