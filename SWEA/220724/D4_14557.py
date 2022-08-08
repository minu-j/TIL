def flip(card):
    if card == 2:
        return 2
    elif card == 1:
        return 0
    elif card == 0:
        return 1

for i in range(int(input())):
    cards = list(map(int, input()))
    done_cards = [2] * int(len(cards))
    while 1 in cards:
        for x in range(len(cards)):
            if cards[x] == 0:
                pass
            elif cards[x] == 2:
                pass
            elif cards[x] == 1:
                cards[x] = 2
                if x == 0:
                    cards[x + 1] = flip(cards[x + 1])
                    pass
                elif x == int(len(cards)-1):
                    cards[x - 1] = flip(cards[x - 1])
                    pass
                else:
                    cards[x + 1] = flip(cards[x + 1])
                    cards[x - 1] = flip(cards[x - 1])
                    continue

    if sum(cards) == sum(done_cards):
        answer = 'yes'
    else:
        answer = 'no'

    print(f'#{i + 1}', answer)