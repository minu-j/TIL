N = int(input())
M = [0, 0, 0, 0, 0, 0]
for _ in range(N):
    now = int(input())
    n1 = M[5] + now
    n2 = M[2] + now
    M = [M[2], M[3], M[4], M[5], n1, n2]
    print(M)
print(max(M))