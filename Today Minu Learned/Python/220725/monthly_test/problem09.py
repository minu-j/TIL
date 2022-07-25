# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if position == (0, 0): # 만약 포지션이 ( )이라면
        if M == 0: # 위치가 범위를 벗어날 경우
            return False #False를 반환
        elif M == 2:
            return False
        else:
            return True

    elif position == (N, N):
        if M == 1:
            return False
        elif M == 3:
            return False
        else:
            return True
    
    elif position[0] == 0:
        if M == 0: 
            return False
        else:
            return True

    elif position[0] == N:
        if M == 1:
            return False
        else:
            return True

    elif position[1] == 0:
        if M == 2:
            return False
        else:
            return True

    elif position[1] == N:
        if M == 3:
            return False
        else:
            return True



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
