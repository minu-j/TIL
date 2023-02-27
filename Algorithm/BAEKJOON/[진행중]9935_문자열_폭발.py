# string = input()
# string = input()
# while True:
#     if string in string:
#         string = string.replace(string, '')
#     else:
#         break
# if string:
#     print(string)
# else:
#     print('FRULA')

string = input()
bomb = input()

stack = ''
ans = ''
for s in string:
    if s not in bomb:
        ans += stack
        stack = ''
        ans += s
    else:
        stack += s
        while True:
            if bomb in stack:
                stack = stack.replace(bomb, '')
            else:
                break

if ans:
    print(ans)
else:
    print('FRULA')