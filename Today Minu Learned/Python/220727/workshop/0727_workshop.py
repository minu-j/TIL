# 1. 아래 명령어는 (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성 하시오.
# $ pip install faker

'''
(1)pip 명령어를 이용하여 faker패키지를 설치한다.
(2)git bash 또는 터미널
'''

# 2. Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다.
# 임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.

from faker import Faker # 1 faker 패키지를 불러오는 명령어이다.
fake = Faker() # 2 Faker는 함수, fake는 변수이다. 
fake.name() # 3 name()은 fake의 메서드이다.

#3.

'''
class Faker():
    def __init__(self, fake):
        pass
'''

#4 - 1.

import random

fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name()) # 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) # 강은주

 # 인스턴스 메서드

#4 - 2.

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name()) # 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) # 강은주
 
 # 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드