town = [0, 0, 0, 0, 0]
while True:
    print(f'현황 : {town}')
    if town == [1, 1, 1, 1, 1]:
         print('방문 배열 완성! : [1, 1, 1, 1, 1]')
         break

    else:
        visit = int(input('방문할 인덱스를 고르세요 : '))

        if visit >= 5 or visit < 0:
            print('==========')
            print('다시 고르자')
            print('==========')
            pass

        else:
            if town[visit] == 0:
                town[visit] = 1
            elif town[visit] == 1:
                pass
        print(town)

