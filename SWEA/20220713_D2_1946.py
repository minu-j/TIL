case = int(input())

list0 = []

i = 0
while i < case:
    count = int(input())
    list1 = []

    j = 0
    while j < count:
        a = 0
        n = 0
        an = 0
        F = input().split()
        a = F[0]
        n = int(F[1])
        list1.append(a*n)
        j += 1
    an = ''.join(list1)
    list0.append(an)
    i += 1

i2 = 0
while i2 < case:
    print('#{}'.format(i2+1))
    com = list0[i2]
    for x in range(0, len(com), 10):
        print(com[x: x + 10])
    i2 += 1
