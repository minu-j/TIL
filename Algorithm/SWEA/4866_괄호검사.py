for tc in range(int(input())):
    word = input()

    stack = []
    ans = 1

    for i in word:
        if i == '{' or i == '(':    # 만약 여는 괄호일 경우?
            stack.append(i)         # 스택에 추가
            continue
        elif i == '}':              # 닫은 괄호일 경우
            if len(stack) <= 0:     # 스택이 비어있으면
                ans = 0             # 오답
                break
            if stack.pop() == '{':  # 스택의 팝이 여는 괄호일 경우
                continue            # 계속
            else:                   # 나머지의 경우
                ans = 0             # 오답
                break
        elif i == ')':
            if len(stack) <= 0:
                ans = 0
                break
            if stack.pop() == '(':
                continue
            else:
                ans = 0
                break
    if len(stack) > 0:              # 스택의 길이가 0보다 길면(남아있는 괄호가 있으면)
        ans = 0                     # 오답

    print(f'#{tc + 1} {ans}')
