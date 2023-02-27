A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]   # 조건에 맞는 리스트 생성

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    ans_count = 0   # 조건에 만족하는 부분집합의 갯수를 카운트할 변수 생성

    for i in range(1 << len(A)):   # 부분집합의 갯수만큼 반복(2의 12제곱)
        subset = []   # 부분집합을 저장할 리스트 초기화

        for j in range(len(A)):   # 리스트의 길이만큼 반복하여 부분집합에 담길 원소 판별
            if i & (1 << j):   # 만약 부분집합에 담을 조건에 만족한다면
                subset.append(A[j])   # 부분집합 리스트에 추가

        if len(subset) == N:   # 해당 부분집합의 길이가 N과 같고,
            if sum(subset) == K:   # 부분집합의 합이 K와 같다면
                ans_count += 1   # 카운트 +1

    print(f'#{tc + 1} {ans_count}')   # 반복문이 모두 종료되면 정답을 출력