def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
ssafy('가흔')

# (2)
ssafy(location='부울경', name='승현')

# (3)
ssafy('지우', location='서울')

# (4)
# ssafy(name='승호', '광주') 
# '광주'의 입력이 어디에 되어야 하는지 특정되지 않아 오류 발생

# 수정한다면?
ssafy(name='승호', location = '광주') 
