# 탑의 부분집합을 구한 후, 합이 B보다 큰 탑만 골라내는 함수
def powerset(depth):
    if depth == N:
        for i in range(len(check)):
            if check[i] == 1:
                check[i] = arr[i]
        if sum(check) >= B:
            tops.append(sum(check))
        return
    check[depth] = 0
    powerset(depth + 1)

    check[depth] = 1
    powerset(depth + 1)


for tc in range(int(input())):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    tops = []
    check = [0] * N
    powerset(0)

    # 구해진 탑 높이 중 최솟값에서 선반 높이를 뺀 값 출력
    print(f'#{tc + 1} {min(tops) - B}')
