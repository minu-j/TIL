# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_duplicate_id(target_username, username_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    duplicate = False # duplicate를 정의
    for i in range(len(username_list)): # username_list를 체크하는 반복문
        if target_username == username_list[i]: # 타겟이 기존 리스트와 같다면
            duplicate = True # duplicate는 True
        else: # 아니라면 패스
            pass
    return duplicate # duplicate값을 반환


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    target_username = 'jungssafy'
    username_list = ['kimssafy', 'jungssafy']
    print(check_duplicate_id(target_username, username_list)) # True
