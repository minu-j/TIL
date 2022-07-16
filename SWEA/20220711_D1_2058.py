num = int(input())

nnnn = num // 1000

nnn = num - nnnn * 1000
nnn = nnn // 100

nn = num - nnnn * 1000 - nnn * 100
nn = nn // 10

n = num - nnnn * 1000 - nnn * 100 - nn * 10

print(nnnn+nnn+nn+n)
