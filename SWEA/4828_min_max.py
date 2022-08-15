T = int(input()) # 테스트케이스의 갯수 입력

for i in range(T):
    N = int(input()) # 양수의 갯수 입력
    a = list(map(int, input().split())) # 양수 aj

    max_a = min_a = a[0] # max, min에 a리스트의 첫번째 값을 할당

    for j in a[1:]:
        if j > max_a:    # max_a보다 값이 크다면
            max_a = j    # max_a에 해당 값을 할당
        elif j < min_a:  # min_a보다 값이 작다면
            min_a = j    # min_a에 해당 값을 할당
        else:
            pass

    print(f'#{i + 1} {max_a - min_a}')  # 최대값 - 최솟값 출력