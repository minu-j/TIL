code_table = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
              '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(int(input())):
    N, M = map(int, input().split())

    # 16진수 암호 추출하기
    passcode_hex_set = set()
    for _ in range(N):
        row = input().split('0')
        for code in row:
            if code:
                passcode_hex_set.add(code)

    print(passcode_hex_set)

    ans = 0

    # 16진수로 된 암호들을 순회하기
    for passcode_hex in passcode_hex_set:

        # 16진수 암호의 각 자릿수를 4자리의 2진수로 변환하여 리스트 형태로 만들기
        passcode_bin_list = []
        for hex_num in passcode_hex:
            passcode_bin_list.extend(('0' * (4 - len(bin(int('0x' + hex_num, 16))[2:]))) + (bin(int('0x' + hex_num, 16))[2:]))

        print(passcode_bin_list)

        # 2진수 암호 리스트의 뒤쪽에 있는 0 지우기(암호는 0으로 끝나지 않으니까)
        count = 0
        for bin_num in reversed(passcode_bin_list):
            if bin_num == '0':
                count += 1
                print(count)
            else:
                break
        passcode_bin_list = passcode_bin_list[:len(passcode_bin_list) - count]

        # 2진수 암호 리스트의 길이를 56의 배수로 만들기
        passcode_bin_list = passcode_bin_list[len(passcode_bin_list) % 56:]

        # 2진수 암호 리스트의 길이를 56으로 만들기
        passcode_bin_list = passcode_bin_list[::len(passcode_bin_list) // 56]

        passcode_bin = ''.join(passcode_bin_list)

        passcode_int_list = []
        for i in range(0, 56, 7):
            passcode_int_list.append(code_table[passcode_bin[i:i + 7]])

        # 고유번호의 합과 검증코드 확인하기
        odd = 0
        even = 0
        test_code = 0
        for idx, int_num in enumerate(passcode_int_list):
            if idx == 8:
                test_code = int_num
            elif idx % 2 == 0:
                odd += int_num
            else:
                even += int_num

        if (odd * 3 + even + test_code) % 10 == 0:
            ans += sum(passcode_int_list)

    print(f'#{tc + 1} {ans}')
