T = int(input()) # 테스트케이스의 갯수

for i in range(T):
    N = int(input())
    cards = map(int, list(input()))
    count_cards = [0] * 10 # 카드의 갯수만큼 빈 카운트 리스트 생성

    for j in cards:   # 각 숫자별 카드의 갯수 카운트
        for k in range(10):
            if j == k:
                count_cards[k] += 1

    max_count_card = 0   # 가장 많은 카드의 갯수를 저장할 변수

    for j in range(10):   # 가장 많은 카드의 갯수와 숫자를 저장
        if count_cards[j] >= max_count_card:
            max_count_card = count_cards[j]
            max_card = j

    print(f'#{i + 1} {max_card} {max_count_card}')