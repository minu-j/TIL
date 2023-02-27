for tc in range(int(input())):
    stack = list(input())
    open = close = 0

    for i in range(len(stack)):
        test = stack.pop()
        if test == "(":
            open += 1
        elif test == ")":
            close += 1

    if open == close:
        print(f'#{tc + 1}', 1)
    else:
        print(f'#{tc + 1}', -1)