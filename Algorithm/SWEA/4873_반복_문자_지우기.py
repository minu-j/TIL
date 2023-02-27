for tc in range(int(input())):
    word = input()
    stack = ['*']   # 1, 2번째 문자가 동일해서 스택이 비어버릴 수 있기때문에 임의 문자를 하나 추가해놓고

    for i in range(len(word)):
        current = stack[-1]
        if current == word[i]:      # 해당 글자가 스택 맨 마지막 자리와 같다면 스택을 팝
            stack.pop()
        else:                       # 아닐 경우 스택에 글자를 쌓기
            stack.append(word[i])
    stack.pop(0)                    # 확인이 끝나면 처음에 추가했던 임의 문자를 제거
    print(f'#{tc + 1} {len(stack)}')
