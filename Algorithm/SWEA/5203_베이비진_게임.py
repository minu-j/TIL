for tc in range(int(input())):
    cards = list(map(int, input().split()))

    count = {'player1': [0] * 12,   # 각 플레이어의 카드 갯수를 셀 딕셔너리
             'player2': [0] * 12}

    winner = 0

    # 카드를 뽑는 순서대로 반복문 진행
    for idx, card in enumerate(cards):
        if idx % 2 == 0:                   # 교대로 카드 뽑아서 숫자 카운트
            count['player1'][card] += 1
        else:
            count['player2'][card] += 1

        if idx > 3:   # 카드를 세개 이상 뽑은 시점부터 검증
            for num in range(10):   # 카운트함수를 돌아봤을때 run이거나 triplet이면 반복문 종료
                if count['player1'][num] >= 3 or count['player1'][num] >= 1 and count['player1'][num + 1] >= 1 and count['player1'][num + 2] >= 1:
                    winner = 1
                    break
                elif count['player2'][num] >= 3 or count['player2'][num] >= 1 and count['player2'][num + 1] >= 1 and count['player2'][num + 2] >= 1:
                    winner = 2
                    break
        if winner:
            break

    print(f'#{tc + 1} {winner}')
