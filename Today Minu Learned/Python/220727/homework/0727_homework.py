# 1. Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.

print(type(int))
print(type(str))
print(type(list()))
print(type(type))
print(type(tuple()))
print(type(dict()))

# 2. 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

'''
    1. __init__ : 인스턴트 객체가 생성될 때 자동으로 호출되는 메서드(생성자 메서드)
    2. __del__ : 인스턴스 객체가 소멸되기 직전 호출되는 메서드(소멸자 메서드)
    3. __str__ : 해당 객체의 출력 형태를 지정(문자열)
    4. __repr__ : 해당 객체를 문자열화 함
'''

# 3. .sort() 와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 
# 클래스에 정의된 메서드들이었다. 
# 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 
# 그 역할과 함께 작성하시오.

'''
    1. .upper() : 대문자로 변경
    2. .lower() : 소문자로 변경
    3. .capitalize() : 첫 문자를 대문자료 변경
    4. .title() : 각 단어의 첫 글자를 대문자로 변경
'''

# 4. 아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.

'''
    1. ZeroDivisionError : 0으로 나누려고 할 때 발생
    2. NameError : Name space상에 이름이 없을 경우
    3. TypeError : 타입 불일치
    4. IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
    5. KeyError : 해당 키가 존재하지 않는 경우
    6. ModuleNotFoundError : 없는 module을 부르는 경우
    7. ImportError : module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
'''