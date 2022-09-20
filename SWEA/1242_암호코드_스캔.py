for tc in range(int(input())):
    N, M = map(int, input().split())

    # 16진수 암호 추출하기
    passcode_hex_set = set()
    for _ in range(N):
        row = input().split('0')
        for code in row:
            if code:
                passcode_hex_set.add(code)

    for passcode_hex in passcode_hex_set:
        print(passcode_hex)

        for hex_num in passcode_hex:


    ans = 0

    print(f'#{tc + 1} {ans}')
