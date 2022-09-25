import sys
sys.stdin = open("input.txt", "r")


def check_code(l, last_bit, depth):
    code = l[last_bit - (56 * depth) + 1:last_bit + 1:depth]
    if code[0:7] in code_table:
        bin_code_set.add(code)
        visit_bit.extend(list(range(last_bit - (56 * depth), last_bit)))
        return
    else:
        check_code(l, last_bit, depth + 1)


code_table = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
              '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9,
              }

for tc in range(int(input())):
    N, M = map(int, input().split())

    hex_code_set = set()
    bin_code_set = set()

    for _ in range(N):
        hex_code = bin(int(input().strip(), 16))[2:]
        hex_code_set.add('0' * len(hex_code) + hex_code)

    print(hex_code_set)

    for line in hex_code_set:

        visit_bit = []

        for idx, bit in zip(range(len(line)-1, -1, -1), line[::-1]):

            if bit == '1' and idx not in visit_bit:
                check_code(line, idx, 1)

    ans = 0

    for bin_code in bin_code_set:

        passcode = []
        for i in range(0, 56, 7):
            passcode.append(code_table[bin_code[i:i + 7]])

        if ((sum(passcode[0:7:2]) * 3) + (sum(passcode[1:7:2])) + passcode[-1]) % 10 == 0:
            ans += sum(passcode)

    print(f'#{tc + 1} {ans}')
