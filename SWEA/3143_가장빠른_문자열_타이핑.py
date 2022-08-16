for tc in range(int(input())):
    A, B = input().split()
    print(f'#{tc + 1} {len(A.replace(B, "*"))}')