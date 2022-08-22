for tc in range(int(input())):
    N = input()
    push_list = ['+', '-', '*', '/']
    stack = []
    for i in N:
        if i in push_list:
            stack.append(i)
        else:
            print(i, end='')
    for i in range(len(stack)):
        print(stack.pop(), end='')
    print()