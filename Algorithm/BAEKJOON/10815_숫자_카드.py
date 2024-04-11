N, n_set, M = input(), set(map(int, input().split())), input()
print(' '.join(
    ['1' if m in n_set else '0' for m in list(map(int, input().split()))]))
