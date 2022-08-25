for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    students = list(range(1, N + 1))

    for i in arr:
        students.remove(i)

    ans = 0

    print(f'#{tc + 1}', end=' ')
    for i in students:
        print(i, end=' ')
    print()
