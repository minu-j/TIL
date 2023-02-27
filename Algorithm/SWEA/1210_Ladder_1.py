for tc in range(10):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 당첨에서부터 거꾸로 타고 올라가는 구조

    ni = 99   # 시작 행은 마지막 행
    for i in range(100):   # 양옆에 도착했을 때 조건을 만들기 까다로워서, 양옆에 0을 추가해서 범위를 벗어나지 못하게 함
        ladder[i].insert(100, 0)   # 오른쪽에 0 추가
        ladder[i].insert(0, 0)     # 왼쪽에 0 추가

    for j in range(101):
        if ladder[ni][j] == 2:   # 모든 열 중에서 2인 열(당첨인 열)을
            nj = j               # 시작 열로 지정

    while ni > 0:   # 첫번째 행에 도착할 때 까지 반복
        if ladder[ni][nj - 1] == 1 and ladder[ni][nj + 1] == 0:   # 사다리를 타고 올라가다가 왼쪽이 1, 오른쪽이 0이면
            while ladder[ni][nj - 1] > 0:                         # 왼쪽에 0이 나타날 때 까지
                nj -= 1                                           # 왼쪽으로 이동
            ni -= 1                                               # 그리고 한칸 위로
        elif ladder[ni][nj - 1] == 0 and ladder[ni][nj + 1] == 1:   # 사다리를 타고 올라가다가 왼쪽이 0, 오른쪽이 1이면
            while ladder[ni][nj + 1] > 0:                           # 오른쪽에 0이 나타날 때 까지
                nj += 1                                             # 오른쪽으로 이동
            ni -= 1                                                 # 그리고 한칸 위로
        else:         # 위 두가지 경우가 아니면
            ni -= 1   # 그냥 한칸 위로
    print(f'#{T} {nj - 1}')