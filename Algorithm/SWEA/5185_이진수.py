# hex_list = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#             '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#             'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
#
# for tc in range(int(input())):
#     N, HEX = input().split()
#     print(f'#{tc + 1}', end=' ')
#     for i in HEX:
#         print(hex_list[i], end='')
#     print()

for tc in range(int(input())):
    N, HEX = input().split()
    print(f'#{tc + 1}', end=' ')
    for i in HEX:
        print(('0' * (4 - len(bin(int('0x' + i, 16))[2:]))) + (bin(int('0x' + i, 16))[2:]), end='')
    print()