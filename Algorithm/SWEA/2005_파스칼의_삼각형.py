for tc in range(int(input())):
    N = int(input())
    stack = [[1] * N]       # 삼각형의 빗변을 맨 윗줄로 하는 사각형을 먼저 생성
    for i in range(1, N):   # 두번째 줄부터 만들기 위해 1부터 N까지 반복문
        stack.append([1])   # 일단 첫번째 항목은 무조건 1이므로 1을 2차원 리스트로 추가하고
        for j in range(1, N - i):   # 1씩 줄여가면서
            stack[i].append(stack[i - 1][j] + stack[i][j - 1])   # 바로 왼쪽과 위에 있는 숫자를 더해준 값을 추가해줌

    # 이렇게 작성하면, N = 5일 때
    # 1 1 1 1 1
    # 1 2 3 4
    # 1 3 6
    # 1 4
    # 1
    # 이런식으로 직각삼각형이 만들어짐. 이제 45도 회전해서 출력해야 함.

    print(f'#{tc + 1}')     # 먼저 테스트케이스 번호를 출력해주고,
    for i in range(N):      # 삼각형의 높이 N만큼 반복
        for j in range(N):   # 위 사각형의 항을 순회할 2차원 리스트 생성
            for k in range(N):
                if j + k == i:   # 오른쪽 위 대각선 방향의 항목만 출력
                    print(stack[k][j], end=' ')
        print('')   # 한줄 끝나면 줄바꿈

    # 이렇게 출력하면 아래처럼 잘 출력됨
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # 1 4 6 4 1
    # 1 5 10 10 5 1
