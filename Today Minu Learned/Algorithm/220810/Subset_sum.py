T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))

    for i in range(1, 1 << len(arr)):   # 1부터(0번 부분집합은 공집합이므로 더하면 0이 나와서 제외)
        subset = []

        for j in range(len(arr)):   # 해당 tc의 길이만큼 반복

            if i & (1 << j):   # 2진수 값에 해당되는 원소만 부분집합 리스트에 추가
                subset.append(arr[j])

        if sum(subset) == 0:   # 부분집합 내의 값을 모두 더했을 때 0이 되면
            print(f'#{tc + 1} 1')   # 1을 반환하고 종료
            break
        elif i == (1 << len(arr)) - 1:   # 모두 계산이 끝나면(합이 0인 부분집합이 없으면
            print(f'#{tc + 1} 0')   # 0을 반환