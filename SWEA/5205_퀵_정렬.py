for tc in range(int(input())):
    N = int(input())
    print(f'#{tc + 1} {sorted(list(map(int, input().split())))[N // 2]}')
