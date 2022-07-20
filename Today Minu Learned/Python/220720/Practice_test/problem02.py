def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    scores.sort()
    scores = scores[::-1]

    i = scores[0]
    sixty = 0

    while i >= 60:
        sixty += 1
        i = scores[sixty]
    print(sixty)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
