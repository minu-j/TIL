a = int(input('Please input a = '))
b = int(input('Please input b = '))
c = int(input('Please input c = '))

ans_1 = (-b) + ((b * b) - (4 * a * c))**(1/2) / 2 * a
ans_2 = (-b) - ((b * b) - (4 * a * c))**(1/2) / 2 * a

print(ans_1, ans_2)