case = int(input())
num = case

listcase = []

i1 = 0
while i1 < case:
    c = input()
    listcase.append(c)
    i1 += 1

count = 0
while count < case:
    text = listcase[count]
    count += 1
    if text == text[::-1]:
        print('#{}'.format(count), 1)
    elif text != text[::-1]:
        print('#{}'.format(count), 0)
