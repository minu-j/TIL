T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in arr:   # 길이가 길어서 일단 만만한 버블정렬로 오름차순 정렬
        for j in range(N - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    sorted_arr = []   # 특별한 정렬이 된 리스트를 저장할 빈 리스트 생성

    for i in range(N // 2):   # N의 절반만큼만 반복해서
        sorted_arr.append(arr[N - i - 1])   # 맨 끝자리를 저장하고
        sorted_arr.append(arr[i])   # 맨 첫자리를 저장하고

    if N % 2 == 1:   # 홀수일 경우 가운데에 있는 수를 리스트 맨 마지막에 저장
        sorted_arr.append(arr[N // 2])

    print(f'#{tc + 1}', end=' ')
    for i in range(10):   # 10번째 숫자까지만 출력
        print(sorted_arr[i], end=' ')
    print('')