n = int(input('1 이상, 1,000 이하의 정수 값을 입력해주세요 : '))

i = 1
div = []

while i <= n:
    if n % i == 0:
        div += [i]
    else:
        pass
    i += 1
print(div)