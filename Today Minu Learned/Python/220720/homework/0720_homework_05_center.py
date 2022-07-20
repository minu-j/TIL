def get_middle_char(x):
    middle_num = int(len(x) / 2) # 글자의 길이 / 2

    if len(x) % 2 == 0: # 글자가 짝수일 경우
        print(x[(middle_num-1):(middle_num+1)])
    else: # 글자가 홀수일 경우
        print(x[middle_num])

get_middle_char('ssafy')
get_middle_char('coding')