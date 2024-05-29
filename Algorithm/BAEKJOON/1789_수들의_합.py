N, S = 0, int(input())
while N < S:
    N += 1
    if N < S:
        S -= N
print(N)