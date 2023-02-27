for tc in range(10):
    N, case, ans = int(input()), input(), 1
    dict_case = {'open': ['(', '[', '{', '<'],   # 여는 괄호와 닫는 괄호 딕셔너리
                 'close': [')', ']', '}', '>']}

    stack = ['*']   # 스택이 빌 경우를 대비해서 임의문자 하나 채우기

    for i in case:
        if i in dict_case['open']:   # 문자열이 open 안에 있으면 스택에 추가
            stack.append(i)
        else:                        # 나머지 경우 스택에서 한개 팝
            current = stack.pop()
            if len(stack) == 0:      # 스택이 빌 경우 임의문자가 나왔다는 것이므로
                ans = 0              # 오답
                break                # 종료
            idx = dict_case['open'].index(current)   # 여는 괄호 인덱스와
            if dict_case['close'].index(i) == idx:   # 닫는 괄호 인덱스가 같아야지만
                continue                             # 넘겨버림
            else:         # 다르면
                ans = 0   # 오답
                break
    if len(stack) > 1:   # 스택이 남아있는 경우에도
        ans = 0          # 오답

    print(f'#{tc + 1} {ans}')