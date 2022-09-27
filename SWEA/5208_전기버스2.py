def charge(n, b):
    global count
    global ans

    if b < 0 or count >= ans:   # 배터리가 0보다 떨어져버리거나, 교환 횟수가 정답 이상이 되면 종료
        return

    if n == arr[0]:     # 도착점에 도착 성공한 경우 교환횟수가 정답보다 작으면 해당 횟수를 정답으로
        if count < ans:
            ans = count
        return

    # 두가지 경우를 재귀
    charge(n + 1, b - 1)   # 배터리 교환 안하고 넘어가는 경우
    if arr[n] > b:   # 해당 정류장의 배터리가 남은 배터리 용량보다 크면?
        count += 1
        charge(n + 1, arr[n] - 1)   # 배터리 교환하고 넘어가는 경우
        count -= 1


for tc in range(int(input())):
    arr = list(map(int, input().split()))

    count = 0
    ans = 99999999999999999999
    charge(1, arr[1])

    print(f'#{tc + 1} {ans}')
