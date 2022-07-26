import random

print('=============================')
print('       Battle Ship Game')
print('           Start !!')
print('=============================')

player = [0] * 15
player_attack = [False] * 15
computer = [0] * 15
computer_attack = [False] * 15

player_position = int(input('배를 위치시킬 시작점을 고르세요. : ')) - 1
if player_position > 12:
    player_position = 12
player[player_position] += 1
player[player_position + 1] = player[player_position + 2] = player[player_position]

computer_position = random.randint(0, 12)
computer[computer_position] += 1
computer[computer_position + 1] = computer[computer_position + 2] = computer[computer_position]

count = 1
while True:
    print('------------------------------------------------------------------------')
    print('Information Board')
    print(f'플레이어의 해역: {player}')
    print(f'플레이어의 공격 기록: {player_attack}')
    print('------------------------------------------------------------------------\n ')

    while True:
        player_attack_num = int(input('공격할 위치를 선택하세요 : ')) - 1
        if player_attack[player_attack_num] == True:
            print('이미 공격한 위치를 선택하셨습니다. 다시 선택해주세요.')
            continue
        else:
            break

    while True:
        computer_attack_num = random.randint(0, 14)
        if computer_attack[computer_attack_num] == True:
            continue
        else:
            break


    if computer[player_attack_num] == 1:
        print(f'<{count}라운드 결과!>')
        print(f'컴퓨터의 해역 : {computer}')
        print(f'플레이어는 컴퓨터의 해역 {player_attack_num + 1}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.\n게임이 종료되었습니다! {count}라운드 만에 플레이어의 승리입니다!')
        break

    elif player[computer_attack_num] == 1:
        print(f'<{count}라운드 결과!>')
        print(f'플레이어는 컴퓨터의 해역 {player_attack_num + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!\n컴퓨터는 플레이어의 해역 {computer_attack_num + 1}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.\n게임이 종료되었습니다! {count}라운드 만에 컴퓨터의 승리입니다!')
        break

    else:
        print(f'<{count}라운드 결과!>')
        print(f'플레이어는 컴퓨터의 해역 {player_attack_num + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!\n컴퓨터는 플레이어의 해역 {computer_attack_num + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
        count += 1
        player_attack[player_attack_num] = True
        computer_attack[computer_attack_num] = True







