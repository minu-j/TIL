num = int(input('숫자를 입력해주세요 : '))

i = 0

for i in range(0 ,num):
    stars = '*' * (i + 1)
    blank = ' ' * (num - i)
    print(f'{blank}{stars}')
    i += 1