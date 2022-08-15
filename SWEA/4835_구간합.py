T = int(input()) # 테스트케이스의 갯수

for i in range(T):
    N, M = map(int, input().split())     # 정수의 갯수와 구간의 갯수
    v = list(map(int, input().split()))  # N개의 정수가 들어있는 배열 v

    sum_list = []   # 정수의 합을 저장할 리스트 생성

    for j in range(N - M + 1):   # M 길이의 정수 합을 sum_list에 추가하는 것을 반복할 반복문
        sum_a = 0                # 더한 값을 저장할 변수 생성

        for k in range(M):       # M 길이의 정수를 더할 반복문
            sum_a += v[j + k]

        sum_list.append(sum_a)   # M길이의 정수 합을 sum_list에 추가

    max_a = min_a = sum_list[0]  # max, min에 sum_list의 첫번째 값을 할당

    for k in sum_list[1:]:       # max, min을 비교하여 저장할 반복문
        if k > max_a:     # max_a보다 값이 크다면
            max_a = k     # max_a에 해당 값을 할당
        elif k < min_a:   # min_a보다 값이 작다면
            min_a = k     # min_a에 해당 값을 할당
        else:
            pass

    print(f'#{i + 1} {max_a - min_a}')  # 최대값 - 최솟값 출력