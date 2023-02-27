def check(l):
    n = 0
    for lan in LAN:
        n += lan // l
    if n >= N:
        return True
    else:
        return False


K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

left = 1
right = 2 ** 32

for _ in range(len(str(2 ** 31)) - 1, -1, -1):
    unit = int('1' + '0' * _)
    for num in range(left, right + 1, unit):
        if not check(num):
            if unit != 1:
                left = num - unit
                right = num
                break
            else:
                print(num - 1)
                exit(0)