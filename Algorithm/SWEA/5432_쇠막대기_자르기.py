T = int(input())

for tc in range(T):
    case = input()
    stick = 0   # 현재 쌓여있는 막대기의 갯수
    cut_stick = 0   # 잘린 막대기의 누적 갯수

    for idx, i in enumerate(case):
        if idx == len(case) or i == ')':   # 만약 마지막 괄호이거나, 닫는 괄호일 경우
            if case[idx - 1] == '(':   # 이전이 닫는 괄호(레이저)일 경우 아무것도 안함
                pass
            else:   # 나머지 경우에는 막대기가 끝나는 경우이므로
                stick -= 1   # 막대기 갯수 -1
                cut_stick += 1   # 잘린 막대기 갯수 +1
        else:   # 그럼 여는 괄호일 경우
            if case[idx + 1] == '(':   # 바로 다음 막대기가 여는 괄호이면 막대기가 추가되는거니까
                stick += 1   # 막대기 갯수 +1
            else:   # 아니라면 레이저이므로
                cut_stick += stick   # 막대기 갯수만큼 잘린 막대기 갯수 +1

    print(f'#{tc + 1} {cut_stick}')