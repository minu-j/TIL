def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.

    last_id = list(user_data['id'][-1::])
    
    if last_id == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        num = True
    else:
        num = False
    
    return(num)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False