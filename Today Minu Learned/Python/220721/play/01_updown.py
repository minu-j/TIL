import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    numb = 0
    print(answer)
    retry = True
    game = True
    while retry == True:
        while game == True:
            counts += 1
            numb = int(input('1이상 10000이하의 숫자를 입력하세요. : '))
            if numb <= 0:
                print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.\n')
                continue
            elif numb > 10000:
                print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.\n')
                continue
            elif numb == answer:
                print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.\n')
                game = False
            elif 10000 >= numb >= 1:
                print('Up!!!\n') if numb < answer else print('Down!!!\n')
        break
    retry = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요 : \n')
    if retry == 'y':
        continue
    elif retry == 'n':
        retry = False
    break
        