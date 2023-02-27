for tc in range(int(input())):
    input()
    print(f'#{tc + 1} {len(max(list(input().split("0")), key=lambda x: sum(map(int, x))))}')
