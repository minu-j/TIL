num = int(input())
N = input().split()

N = list(map(int, N))
N.sort()

num = num // 2

c = int(N[num])

print(c)
