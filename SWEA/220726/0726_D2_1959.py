case = int(input())
n = []
m = []
ai = []
bj = []

for i in range(case):
    nm = list(input().split())
    n.append(int(nm[0]))
    m.append(int(nm[1]))

    a = []
    b = []

    a = input().split()
    b = input().split()

    ai.append(a)
    bj.append(b)

print(n, m, ai, bj)