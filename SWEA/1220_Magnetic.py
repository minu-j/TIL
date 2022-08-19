for tc in range(10):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 1은 아래로 내려가고, 2는 위로 올라가려는 성질이 있음.
    # 1 = N극 / 2 = S극

    count = 0   # 전체 교착 갯수

    for i in range(N):
        stack = []                      # N극을 저장해놓을 스택, 아래가 비어있다면 그대로 떨어지므로 다음 줄에 갈 때 초기화되어야 함.

        for j in range(N):
            if matrix[j][i] == 0:       # 비어있는 경우 제외
                continue
            elif matrix[j][i] == 1:     # N극인 경우 아래로 내려가려 함.
                stack.append(1)         # 아래에 S가 있는지 봐야하므로 스택에 저장해놓음.
            elif matrix[j][i] == 2:     # S극인 경우 위로 올라가려 함.
                if len(stack) == 0:     # 스택이 비어있으면, 위에 교착이 있다면 해당 교착에 붙어버리고,
                    continue            # 없다면 떨어지므로 카운트에 영향을 미치지 않음.
                else:
                    stack.clear()       # S극에 부딪히면 N극이 전부 교착되므로 초기화
                    count += 1          # 교착 +1

    print(f'#{tc + 1} {count}')
