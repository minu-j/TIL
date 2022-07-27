# Python

## 들어가며...

* **소스코드 :** 프로그래밍 언어로 작성된 프로그램(사람이 이해하고 작성할 수 있음)

* **번역기(interpreter/compiler) :** 소스코드를 컴퓨터가 이해할 수 있는 기계어로 번역

* 파이썬은 사람 친화적(High level)인 언어이다.

* **인터프리터 언어(Interpreter) :** 소스코드를 기계어 변환할 때 통역하듯 1줄씩 변환
- **객체지향 프로그래밍(Object Oriented Programming)**

- **파이썬의 개발환경 :** IDE, Jupyter Notebook 등
* **스타일 가이드 :** 코드를 어떻게 작성할 것인가에 대한 가이드
  (파이썬 코드 스타일 가이드 PEP8 http://www.python.org/dev/peps/pep-0008/)

* 파이썬 프로그램의 구성 단위
  
  * 식별자
  * 리터럴
  * 표현식 : 새로운 데이터 값을 생성하거나 계산하는 코드 조각
  * 문장 : 특정한 작업을 수행하는 코드, 최소환의 코드 단위

---

## 파이썬 기초

### 주석(Comment)

> 코드에 대한 설명, 코드를 이해하기 쉽게 함 
> (주석은 실행속도에 영향을 주지 않음 -> 주석을 작성하는 습관을 들여야 함.)

* 한줄 주석 : 주석으로 처리될 내용 앞에 #을 붙힘
* 여러줄 주석 : 문장 위 아래에 ''' 또는 """을 묶어서 표현

### 변수(Variable)

> 데이터를 저장하기 위해 사용, 복잡한 값들을 쉽게 사용**(추상화)**

**식별자(변수 이름의 규칙)ㅑ

1. 첫 글자에 숫자가 올 수 없음

2. 길이 제한이 없고, 대소문자를 구별

3. 예약어(reserved words) 사용 불가(False, if...)
   
   ```python
   import keyword
   print(keyword.kwlist)
   ```

4. 내장함수, 모듈 이름 사용하지 않아야 함

### 연산자(Operator)

산술 연산자(Arithmetic Operator)

| 연산자 | 내용  | 연산자 | 내용   |
|:---:|:---:|:---:| ---- |
| +   | 덧셈  | -   | 뺄셈   |
| *   | 곱셈  | /   | 나눗셈  |
| //  | 몫   | **  | 거듭제곱 |

### 자료형(Datatype)

1. 수치형(Numeric Type)
   
   1. 정수 자료형(int)
   2. 실수 자료형(float) : 유리수와 무리수를 포함하는 '실수'
      * 실수 연산시 주의할 점(부동소수점) : 컴퓨터는 2진수를 사용하기 때문에 실수 계산시 매우 작은 오차 발생

2. 문자형(String Type)
   
   * 문자열은 앞뒤에 작은따옴표(')나 큰 따옴표(")를 활용
     
     * 문자열을 묶을 때 동일 문장부호 활용, 한가지 문장부호를 지속 사용 권장
   
   * 중첩 따옴표 : 작은따옴표 내 큰 따옴표, 큰 따옴표 내 작은 따옴표 작성
   
   * 삼중 따옴표 : 작은 따옴표나 큰 따옴표 삼중('''/""")사용(따옴표 안에 따옴표 표기시)
   
   * Escape sequence
     
     | 예약문자 | 내용(의미)    | 예악문자 | 내용(의미)    |
     |:----:|:---------:|:----:|:---------:|
     | \n   | 줄 바꿈      | \t   | 탭         |
     | \r   | 캐리지 리턴    | \0   | 널(Null)   |
     | \\\  | \\        | \\'  | 단일인용부호(') |
     | \\"  | 이중인용부호(") |      |           |
   
   * 문자열 연산
     
     * 덧셈 : 문자열 덧셈은 문자열을 연결(String Concatenation)
       
       ```python
       print("hello"+"Worle") # HelloWorld
       ```
     
     * 곱셈
       
       ```python
       print("python"*3) # pythonpythonpython
       ```
   
   * String Interpolation
     
     * f-string(python 3.6+)
       
       ```python
       print(f'{}')
       
       import datetime
       today = datetime.datetime.now()
       print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
       #오늘은 2022년 7월 18일
       
       pi = 3.141592
       print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
       # 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
       ```

3. 불린형(Boolean Type) : 논리 자료형으로 참과 거짓을 표현(True/False)
   
   * 비교 연산자
     
     | 연산자 | 내용       | 연산자    | 내용       |
     |:---:|:--------:|:------:|:--------:|
     | <   | 미만       | <=     | 이하       |
     | >   | 초과       | >=     | 이상       |
     | ==  | 같음       | !=     | 같지않음     |
     | is  | 객체 아이덴티티 | is not | 객체 아이덴티티 |
   
   * 논리 연산자
     
     | 연산자     | 내용                         |
     |:-------:|:--------------------------:|
     | A and B | A와 B 모두 True시, True        |
     | A or B  | A 와 B 모두 False시, False     |
     | Not     | True를 False로, False를 True로 |

4. 논리 연산자 주의할 점
   
   * Falsy(False는 아니지만 False로 취급) : 0, 0.0, (), [], {}, None, ""(빈 문자열)
   
   * 논리 연산자도 우선순위가 존재 : not, and, or순으로 우선순위가 높음
   
   * 단축평가 : 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
     
     * and 연산에서 첫번째 값이 False인 경우 무조건 False -> 첫번째 값 반환
     
     * or 연산에서 첫번째 값이 True인 경우 무조건 True -> 첫번째 값 반환
     
     * 0은 False, 1은 True

5. None : 값이 없음을 표현하기 위한 문자열
   
   > ```python
   > a = [1, 2]
   > 
   > a[bool([])] # 1
   > ```

---

## 데이터의 저장

### 컨테이너

> 여러개의 값(데이터)를 담을 수 있는 객체로 서로 다른 자료형을 저장할 수 있음

- 컨테이너의 분류
  
  1. 시퀀스형 : 순서가 있는(Ordered) 자료구조 - 리스트, 튜플, 레인지
     
     1. 리스트 : 여러개의 값을 순서가 있는 구조로 저장 **- 가변자료형**
        
        ```python
        [] 또는 list()를 통해 생성
        ```
        
        * 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
          
          ```python
          list[i]
          ```
     
     2. 튜플 : 여러개의 값을 순서가 있는 구조로 저장 **- 불변자료형**
        
        ```python
        () 또는 tuple()를 통해 생성
        ```
        
        * 생성시 주의사항
          
          * 단일 항목 : 하나의 항목으로 구성된 튜플은 생성시 값 뒤 쉼표를 붙혀야 함
          
          * 복수 항목 : 마지막 항목에 쉼표는 없어도 되지만, 넣는 것을 권장
        
        * 튜플 대입(Tuple assignment) : 우변의 값을 좌변의 변수에 한번에 할당하는 과정
          일반적으로 파이썬 내부에서 활용
     
     3. 레인지 : 숫자의 시퀀스를 나타내기 위해 사용(주로 반복문과 함게 사용)
        
        ```python
        range(n) # 기본형 - 0부터 n-1까지 숫자의 시퀀
        range(n, m) # 범위 지정 - n부터 m-1까지 숫자의 시퀀스
        range(n, m, s) # 범위 및 스텝 지정 - n부터 m-1까지 s만큼 증가하는 숫자의 시퀀스
        ```
     * 슬라이싱 연산자 : 시퀀스를 특정 단위로 슬라이싱
       
       ```python
       # 리스트([1:4]에서 1은 포함, 4는 미포함)
       print([1, 2, 3, 5][0:4:2]) #[1, 3]
       
       # 튜플
       print((1, 2, 3, 5)[0:4:2]) #(1, 3)
       
       # range
       print(range(10)[1:5:3]) #range(1, 5, 3)
       
       #문자열
       print('abcdefg'[1:3:2]) #b
       ```
  
  2. 비시퀀스형 : 순서가 없는(Unordered) - 세트, 딕셔너리
     
     1. 셋(Set) : 중복되는 요소가 없이 순서에 상관없는 데이터들의 묶음 **- 가변자료형**
        
        ```python
        {} 또는 set()를 통해 생성
        # 빈 셋을 만들기 위해서는 반드시 set()
        ```
        
        * 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있으면 하나만 저장
        
        * 순서가 없기 때문에 인덱스를 이용한 접근 불가능
        
        * 수학에서의 집합을 표현한 컨테이너
        
        * 집합 연산이 가능(합집합, 차집합, 교집합(여집합은 없음))
        
        * 중복된 값이 존재하지 않음셋을 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음
          (단, 이후 순서가 무시됨)
        - 셋 연산자(여집합은 없음)
          
          | 연산자 | 내용  | 연산자 | 내용    |
          |:---:|:---:|:---:|:-----:|
          | \|  | 합집합 | &   | 교집합   |
          | -   | 차집합 | ^   | 대칭차집합 |
     
     2. 딕셔너리(Dictionary)
        
        ```python
        {} 또는 dict()를 통해 생성
        ```
        
        * 키-값(key-value) 쌍으로 이뤄진 자료형 **- 3.7+ orderd, 이하버전은 unordered**
          * Dictonary의 Key : 변경 불가능한 데이터만 활용 가능
            string, interger, float, boolean, tuple, range
          * 각 key의 값은 어떤 형태이든 상관 없음

### 형 변환

> 파이썬에서 데이터 형태는 서로 변환할 수 있음.

- 암시적 형 변환(Implicit) : 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
  
  1. bool
  
  2. Numeric type (int, float)
     
     ```python
     print(True + 3) # 4 (자동으로 boolean -> 정수)
     print(3 + 5.0) # 8.0 (자동으로 정수 -> 실수)
     ```

- 명시적 형 변환(Explicit) : 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
  
  1. int (str, float -> int) : 단, 형식에 맞는 문자열만 정수로 변환 가능
     
     ```python
     print('3' + 4) # TypeError : 문자열은 암시적 타입 변환이 되지 않음.
     
     print(int('3') + 4) # 7
     
     print(int('3.5') + 5) #ValueError : 3.5는 정수가 아니므로 타입 변환되지 않음.
     ```
  
  2. float (str, int -> float) : 단, 형식에 맞는 문자열만 float로 변환 가능
     
     ```python
     print('3.5' + 3.5) # TypeError
     
     print(float('3')) # 3.5
     
     print(float('3/4') + 5.3) #ValueError
     ```

> input()을 이용한 사용자 데이터 입력은 숫자도 문자열로 저장됨.

---

## 데이터의 처리

### 제어문(Control statement)

> 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행하나,
> 
> 특정 상황에 따라 코드를 선택적으로 실행하거나 반복하는 제어가 필요함.

1. ​    조건문 : 참/거짓을 판단할 수 있는 조건식과 함께 사용
   
   * 기본 형식 : 참/거짓에 대한 조건식(if/else)
     
     ```python
     if a > 5: # 조건식이 참일 경우 아래 내용 실행
         print('5 초과')
     else: # 거짓일 경우 아래 내용 실행
         print('5 이하')
     ```
   
   * 복수 조건문 : 복수의 조건식을 활용(elif)
     
     ```python
     if 조건:
         # code block
     elif 조건:
         # code block
     else:
     ```
   
   * 중첩 조건문 : 조건문은 다른 조건문에 중첩되어 사용될 수 있음.
     
     ```python
     if 조건:
         # code block
         if 조건:
             # code block
     else:
     ```
   
   * 조건 표현식 : 조건문을 한 줄로 표현하는 식
     
     > 삼향연산자(Ternary Operator)로 부르기도 함
     
     ```python
     "True인 경우 값" if 조건 else "False인 경우 값"
     ```
     
     ```python
     # 조건문
     num = 2
     if num % 2:
         result = '홀수입니다.'
     else:
         result = '짝수입니다.'
     print(result)
     
     # 조건표현식
     num = 2
     result = '홀수입니다.' if num % 2 else '짝수입니다.'
     print(result)
     ```

2. 반복문 : 특정 조건을 만족할 때 까지 같은 동작을 계속 반복하고 싶을 때 사용
   
   * 반복문의 종류
     
     1. while 문 : 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
     2. for 문 : 반복 가능한 객체를 모두 순회하면 종료(별도 종료조건이 필요 없음)
     3. 반복 제어 : break, continue, for-else
   
   * while 문  : 조건이 참인 경우 반복적으로 코드를 실행
     
     > 코드블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
     > 
     > while문은 종료조건이 반드시 필요
     
     ```python
     while 조건:
        # code block
     ```
     
     * 복합 연산자 : 연산과 할당을 합쳐 놓은 것(+=, *=)
   
   * for 문 : 시퀀스의 마지막 값에 접근할 때 까지 반복적으로 코드를 실행
     
     > 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(Iterable)의 요소를 모두 순회하며, 처음부터 끝까지 모두 순회하므로 별도 종료 조건이 필요하지 않음.
     > 
     > * iterable
     >   * 순회할 수 있는 자료형(string list, dict, tuple, range, set 등
     >   * 순회형 함수(range, enumerate)
     
     ```python
     for 변수명 in itrable:
         # code block
     ```
     
     * 딕셔너리 순회 : 기본적으로 key를 순회하며, key를 통해 값을 활용
       
       ```python
       grades = {'john': 80, 'eric': 90}
       for student in grades:
           print(student)
       
       # john
       # eric
       ```
       
       추가 메서드를 활용한 딕셔너리 순회
       
       * keys() : key로 구성된 결과
       * values() : value로 구성된 결과
       * items() : (key, value)의 튜플로 구성된 결과
       
       ```python
       grades = {'john': 80, 'eric': 90}
       
       print(grades.keys())
       print(grades.values())
       print(grades.items())
       
       #dict_keys {['john', 'eric']}
       #dict_values {[80, 90]}
       #dict_items {[('john', 80), ('eric', 90)]}
       
       for student, grade in grades.items():
           print(students, grade)
       
       # john 80
       # eric 90
       ```
     
     * enumerate 순회
       
       * enumerate() : (index, value) 형태의 tuple로 구성된 열거 객체를 반환
       
       ```python
       members = ['민수', '영희', '철수']
       
       for idx, number in enumerate(members):
           print(idx, number)
       
       # 0 민수
       # 1 영희
       # 2 철수
       ```
       
       ```python
       print(list(enumerate(members)))
       # [(0, '민수'), (1, '영희'), (2, '철수')]
       
       print(list(enumerate(members, start = 1)))
       # [(1, '민수'), (2, '영희'), (3, '철수')]
       ```
     
     * List Comperehension : 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성
       
       ```python
       [code for 변수 in iterable]
       
       [code for 변수 in iterable if 조건식]
       ```
       
       ```python
       cubic_list = []
       for number in range(1, 4)
           coubic_list.append(number ** 3)
       print(cubic_list)
       
       cubic_list = [number ** 3 for number in range(1,4)]
       print(cubic list)
       # 위와 동일 출력
       ```
     
     * Dictionary Comprehension
       
       ```python
       {key: value for 변수 in iterable}
       {key: value for 변수 in iterable if 조건식}
       ```
       
       ```python
       cubic_dict = {}
       for number in range(1, 4)
           coubic_dict[number] = number ** 3
       print(cubic_dict)
       
       cubic_dict = {number: number ** 3 for number in range(1,4)}
       print(cubic dict)
       # 위와 동일 출력
       ```
* 반복문 제어
  
  * break : 반복문을 종료
    
    * for, while문을 파괴시킴(가장 가까운 반복문)
      
      ```python
      houses = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
      
      ready = True
      
      for house in houses:
          if house == 1:
              ready = False
              break  # 브레이크!!! : 
                     # 10번을 연산해야 하나, 1이 나오는 즉시 break
      
      print(ready)
      ```
  
  * continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
  
  * for-else : 끝까지 반복문을 실행한 이후에 한번도 걸리지 않았다면 else문 실행
    
    * break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
      
      > 알고리즘 문제에서 For - Else 구문은,
      > 
      > for 쪽에는 → 왠지 하나라도 조건에 안맞을거 같은 것들을 검사해 보고
      > 
      > `단 하나`라도 조건에 안맞는 경우 `break` 가 걸리게끔 설정해 두고
      > 
      > Else 쪽에는 → `완주 축하!` 처럼 어라? 위에서 단 하나도 안걸렸다고? 그러면 전부 테스트를 통과한거니까 그 경우 실행할 로직을 적자! 느낌으로 문제가 풀이되게 됩니다.
  
  * pass : 아무것도 하지 않음(문법적으로 필요하지만 할 일이 없을 때)

---

### 함수(Function)

* 특정한 기능을 하는 코드의 조각(묶음)
* 특정 코드를 매번 다시 작성하지 않고 필요시에만 호출하여 간편히 사용

### 함수를 왜 사용할까?

1. Decomposition(분해) : 기능을 분해하고 재사용하게 만들고
2. Abstraction(추상화) : 복잡한 내용을 모르더라도 사용할 수 있도록, 재사용성과 가독성
   - 내부 구조를 변경할게 아니면 구조를 몰라도 무방하다

### 함수의 종류

1. 내장함수 : 파이썬에 기본적으로 포함된 함수(파이썬 개발자들이 만들어놓은 함수)
2. 외장함수 : import문을 사용하여 외부 라이브러리에서 제공하는 함수(다른 개발자들)
3. 사용자 정의 함수 : 직접 사용자가 만드는 함수

### 함수의 기본 구조

- 선언과 호출(Define & Call)
- 입력(Input)
- 문서화(Docstring)
- 범위(Scope)
- 결과값(Output)

```python
#keyword, #name, #parameters
def pstdev(data, mu = None)
    '''
    # Docstring
    '''
  var = pvariance(data, mu) # function body
  try:
    return var.sqrt() # return
  except AttributeError:
    return math.sqrt(var)
```

### 함수의 정의

함수를 사용하기 위해서는 먼저 함수를 정의해야 함.

```python
def function_name(parameter):
    #code block
    return returning_value
```

### 선언과 호출

함수는 함수명()으로 호출하여 사용

```python
def foo():
    return True

foo()

def add(x, y):
    return x + y

add(2,3)
```

### 값에 따른 함수의 종류

- Void function : 명시적인 return값이 없는 경우 None을 반환하고 종료
- Value returning function : 함수 실행 후, return문을 통해 값 반환 후 종료

> print함수와 return의 차이점
> 
> - print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
> - 데이터 처리를 위해서는 return 사용

### 함수의 입력

- parameter : 함수를 정의할 때 함수 내부에서 사용되는 변수

- Argument : 함수를 호출할 때 넣어주는 값(함수의 parameter를 통해 전달되는 값)
  
  - 소괄호 안에 할당 : func_name(argument)
  
  - 필수 Argument : 반드시 전달되어야 하는 argument
  
  - 선택 Argument : 값을 전달하지 않아도 경우는 기본값이 전달
  
  - Positional Arguments : 기본적으로 함수 호출시 위치대로 들어감.
  
  - Keyword Arguments : 직접 변수의 이름으로 특정 Argument를 전달
    
    > 단, Keyword Argument 다음에 Positional Argument 활용 불가
    > 
    > ```python
    > add(x = 2, y = 5)
    > add(2, y = 5)
    > add(x = 2, 5) #error
    > ```
  
  - Default Arguments Values : 기본값을 지정하여 함수 호출시 argument값을 설정하지 않도록 함.
    
    ```python
    def add(x, y = 0):
      return x + y
    
    add(2) -> def add(2, y = 0)
    ```
  
  - 정해지지 않은 여러개의 Arguments 처리(print())
    
    : 애스터리스크(*) 사용

- 가변인자(*args) : 여러개의 Positional Arguments를 하나의 필수 parameter로 받아서 사용
  
  - 패킹 : 여러개의 데이터를 묶어서 변수에 할당하는 것
    
    ```python
    numbers = (1,2,3,4,5)
    print(numbers) # (1,2,3,4,5)
    ```
  
  - 언패킹 : 시퀀스 속 요소들을 여러 변수에 나누어 할당하는 것
    
    ```python
    numbers = (1,2,3,4,5)
    a, b, c, d, e = numbers
    print(a, b, c, d, e) # 1 2 3 4 5
    ```
    
    - 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야 함
    
    - 언패킹시 왼쪽 변수에 asterisk(*)를 붙히면 할당하고 남은 요소를 리스트에 담을 수 있음
      
      ```python
      numbers = (1,2,3,4,5)
      
      a, b, *rest = numbers
      print(a, b, rest) # 1 2 [3, 4, 5]
      
      a, *rest, e = numbers
      print(rest) # [2, 3, 4]
      ```
  
  - Asterisk와 가변인자
    
    ```python
    def func(*args):
      print(args)
      print(type(args))
    
    func(1, 2, 3, 'a', 'b')
    
    # (1, 2, 3, 'a', 'b')
    # <class 'tuple'
    ```

> 반드시 받아야 하는 인자와 추가적인 인자를 구분해서 사용할 수 있음.
> 
> ```python
> def print_family_name(father, mother, *pets):
>   print(f'아버지 : {father}')
>   print(f'어머니 : {mother}')
>   print(f'반려동물들.. : {pets}')
> ```

* 가변 키워드 인자(**kwargs)
  
  > 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
  > 
  > ***kwargs는 딕셔너리로 묶여 처리되며, parameter에 \**\*를 붙혀 표현
  
  ```python
  def family(**kwargs):
    for key, value in kwargs.items:
      print(key, ":", value)
  
  family(father = '아버지', mother = '어머니', ...)
  ```
  
  가변인자와 가변 키워드 인자를 함께 사용할 수 있음.

### python의 범위(scope)

* 함수는 코드 내부에 Local scope를 생성하며,
  그 외의 공간인 Global scope로 구분
  
  > - scope
  >   
  >   - global scope : 코드 어디에서든 참조(사용)할 수 있는 공간
  >   
  >   - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
  > 
  > - variable
  >   
  >   - global variable : global scope에 정의된 변수
  >   - local scope : local scope에 정의된 변수

* 변수 수명주기(lifecycle)
  
  * built-in scope : 파이썬이 실행된 이후부터 영원히 유지
  * global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때 까지 유지
  * local scope : 함수가 호출될 때 생성되고 함수가 종료될 때 까지 유지

* 이름 검색 규칙(Name Resolution)
  
  * 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
  
  * LEGB Rule
    
    * Local scope : 지역 범위
    * Enclosed scope : 지역 범위 한 단계 위 범위
    * Global scope : 최상단에 위치한 범위
    * Built-in scope : 모든 것을 담고 있는 범위 ex) print()
    
    > 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
    
    ```python
    a = 0
    b = 1
    def enclosed():
        a = 10
        c = 3
        def local(c):
            print(a, b, c) # 10 1 300
        local(300)
        print(a, b, c) # 10 1 3
    enclosed()
    print(a, b) #0 1
    ```

* global문 : 현재 코드블록 전체에 적용
  
  ```python
  a = 10
  def func1():
      global a
      a = 3
  
  print(a) # 10
  func1()
  print(a) # 3
  ```

* nonlocal : global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함
  
  ```python
  x = 0
  def func1():
      x = 1
      def fun2():
            nonlocal x
          x = 2
      fun2()
      print(x) #2
  
  fun1()
  print(x) #0
  ```

### 함수의 응용

- map(function, iterable)

- filter(function, iterable)

- zip(*iterables)

- lambda[parameter] : 익명의 함수

- 재귀 함수 : 자기 자신을 호출하는 함수
  
  예 ) 팩토리얼
  
  > 재귀함수 주의사항 :  base case에 도달할 때 까지 함수를 호출함.
  > 
  > 메모리 스택이 넘치게 되면 프로그램이 동작하지 않게 됨.
  > 
  > 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000번

---

### 모듈과 패키지

> 외부 개발자들이 만들어놓은 코드를 가져오기 위한 기능

- 모듈(module) : 다양한 기능을 하는 코드를 하나의 파일로 만든 것
  
  - import module
  - from module import var, function, Class
  - from module import *

- 패키지(pakage) : 다양한 파일을 하나의 폴더로 묶은 것
  
  - from package import module
  - from pakage.module import var, function, Class
  
  > - 라이브러리(library) : 다양한 패키지를 하나의 묶음으로
  > - pip : 이것을 관리하는 관리자
  > - 가상환경 : 패키지의 활용 공간

- 파이썬 표준 라이브러리

- 파이썬 패키지 관리자(pip) : pypi에 저장된 외부 패키지들을 설치하도록 도와주는 관리자
  
  - 패키지 설치 : 최신버전/특정버전/최소버전을 명시하여 설치할 수 있음.
  - pip 명령어
    - $ pip list
    - $ pip show pakage
    - $ pip freeze > requirements.txt : 설치된 패키지 목록 출력
    - $ pip intall -r requirements.txt : 패키지 목록대로 설치

- 사용자 모듈과 패키지
  
  - 사용자가 만든 .py파일에 있는 함수를 다른 py파일에서 응용 가능

### 가상환경

> 가상환경을 만들고 관리하는데 사용되는 모듈
> 
> 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음.

---

## 데이터 구조

* 데이터 구조를 활용하기 위해서는 메서드(method)를 활용한다.
  
  * 매서드는 클래스 내부에 정의한 함수(사실상 함수와 동일)
    
    ```python
    데이터구조.메서드()
    ```

### 문자열(string type)

* 문자들의 배열(sequence of characters), 모든 문자는 str타입(변경 불가능한 immutable)

* 문자열 조회/탐색 및 검증 메서드
  
  ```python
  s.find(x) # x의 첫번째 위치를 반환, 없으면 -1을 반환
  s.index(x) # x의 첫번째 위치를 반환, 없으면 오류 발생
  
  s.isalpha(x) # 알파벳 문자 여부(단순 알파벳이 아닌 유니코드상 letter)
  
  s.isupper(x) # 대문자 여부
  s.islower(x) # 소문자 여부
  
  s.istitle(x) # 타이틀 형식 여부
  
  s.isdecimal() # 숫자 여부(가장 엄격하게 숫자인 문자들)
  s.isdigit()  # 숫자 여부(숫자와 비슷하거나 원문자 등도 포함)
  s.isnumeric() # 숫자 여부(분수 형태, 로마자 등의 특수문자도 포함)
  
  s.replace(old, new[,count]) # 대상 문자를 새로운 글자로 바꿔서 반환
  # count : 
  
  s.strip([chars]) # 공백이나 특정 문자를 제거(양쪽)
  s.lstrip() # 왼쪽을 제거
  s.rstrip() # 오른쪽을 제거
  # 문자열을 지정하지 않으면 공백을 제거
  
  s.split(sep=None, maxsplit=-1) # 공백이나 특정 문자를 기준으로 분리
  # sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고 선행/후행 공백은 빈 문자열에 포함시키지 않음.
  
  'separator'.join([interable])
  # 반복 가능한(iterable)컨테이너 요소들을 saparator를 끼워서 문자열 반환
  # iterable에 문자열이 아닌 값들이 있으면 typeerror 발생
  
  s.capitalize() # 문자열의 첫번째 문자가 대문자로
  s.title() # 띄어쓰기 기준 첫번째 문자가 대문자로
  
  s.upper() # 전부 대문자로
  s.lower() # 전부 소문자로
  s.swapcase() # 대소문자 변경
  ```

* 리스트 메서드
  
  ```python
  l.append(x) # 리스트 마지막 항목에 x를 추가
  l.insert(i, x) # 리스트 인덱스 i에 항목 x를 삽입
  
  l.remove(x) # 리스트 왼쪽부터 첫번째의 x를 제거, 없으면 오류
  
  l.pop(i) # 리스트 가장 오른쪽 i를 반환 후 제거
  l.pop() # 리스트 가장 오른쪽 항목을 반환 후 제거
  
  l.extend(m) # 순회형 m의 모든 항목들을 리스트 끝에 추가(+=와 동일)
  
  l.index(x, start, end) # 리스트에 있는 항목 중 가장 왼쪽에 있는 x의 인덱스를 반환
  
  l.reverse() # 리스트를 거꾸로 정렬
  l.sort() # 리스트를 정렬(매개변수 이용 가능)
  
  l.count(x) # 리스트에서 항목 x가 몇개 존재하는지 갯수를 반환
  ```

* 튜플 관메서드 : 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만 지원

* 연산자
  
  * 멤버십 연산자
    
    * in, not in : 포함여부 확인
      
      ```python
      print('a' in 'apple') #True
      ```
    
    * 산술연산자(+)
    
    * 반복 연산자(*)

* 셋 메서드
  
  ```python
  s.copy() # 셋의 얕은 복사본을 반환
  
  s.add(x) # 항목x가 셋에 없다면 추가
  
  s.pop() # 셋s에서 랜덤하게 항목을 반환하고 해당 항목을 제거(순서가 없기 때문에), set이 비어있을 경우 KeyError
  
  s.remove(x) # 항목 x를 삭제, 존재하지 않을 경우 KeyError
  s.discard(x) # 항목x를 삭제, 존재하지 않아도 에러x
  
  s.update(t) # 셋t에 있는 모든 항목 중 셋s에 없는 항목을 추가
  
  s.clear() # 모든 항목을 제거
  
  s.isdisjoint(t) # 셋 s와 t가 서로소인 경우 True
  s.issubset(t) # 셋 s가 t의 하위 셋인 경우 True
  s.issuperset(t) # 셋 s가 t의 상위 셋인 경우 True
  ```

* 딕셔너리 메서드
  
  ```python
  d.clear() # 모든 항목을 제거
  
  d.copy() # 얕은 복사본 반환
  
  d.keys() # 딕셔너리의 모든 키를 담은 뷰를 반환
  d.values() # 딕셔너리의 모든 값을 담은 뷰를 반환
  d.items() # 딕셔너리의 모든 키-값의 쌍을 담은 뷰를 반환
  
  d.get(k) # 키 k의 값을 반환하는데, 키k가 없을 경우 None 반환
  d.get(k, v) # k가 딕셔너리에 없을 경우 v를 반환
  
  d.pop(k) # k값을 반환하고 삭제하는데, 없을 경우 KeyError
  d.pop(k, v) # 없을 경우 v 반환
  
  d.update([other]) # 딕셔너리 리  d의 값을 매핑하여 업데이트
  ```

---

## 얕은 복사와 깊은 복사

* 복사의 방법
  
  * 할당(Assignment)
    
    * 대입연산자(=) : 해당 객체에 대한 객체 참조를 복사(같은 주소)
      
      ```python
      a = [1, 2, 3]
      b = a
      ```

* 얕은 복사(Shallow Copy)
  
  * Slice 연산자를 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사(다른 주소)
    
    ```python
    a = [1, 2, 3]
    b = a[:]
    
    '''
    얕은 복사의 주의사항
    * 리스트 속 리스트의 값은 얕은복사되지 않고 할당됨.
    '''
    
    a = [1, 2, ['a', 'b']]
    b = a[:]
    # a = [1, 2, ['a', 'b']] 
    # b = [1, 2, ['a', 'b']]
    
    b[2][0] = 0
    # a = [1, 2, [0, 'b']] 
    # b = [1, 2, [0, 'b']]
    ```

* 깊은 복사(Deep copy)
  
  ```python
  import copy
  
  a = [1, 2, ['a', 'b']]
  b = copy.deepcopy(a)
  # a = [1, 2, ['a', 'b']] 
  # b = [1, 2, ['a', 'b']]
  
  b[2][0] = 0
  # a = [1, 2, ['a', 'b']] 
  # b = [1, 2, [0, 'b']]
  ```



---



## 객체지향 프로그래밍

> 객체지향 프로그래밍(Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임 중 하나이다. 객체지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.

* 객체
  * 정보(변수)
    * 클래스 변수
    * 인스턴스 변수
  * 행동(함수)

* 객체지향 프로그래밍이 필요한 이유
  * 현실 세계를 프로그램 설계에 반영(추상화)

* 객체지향의 장/단점
  * 장점
    * 클래스 단위로 모듈화시켜 개발할 수 있어 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    * 필요한 부분만 수정하기 쉽기 때문에 프로그램 유지보수가 쉬움
  * 단점
    * 설계시 많은 노력과 시간이 필요 : 다양한 객체들의 상호작용 구조를 만들기 위한 시간과 노력이 필요
    * 실행속도가 상대적으로 느림 : 절차지향 프로그래밍이 컴퓨터 처리구조와 비슷해서 실행속도가 빠름
  > 사람이 편하면, 컴퓨터가 힘들다.



## 객체

> 컴퓨터 과학에서 객체 또는 오브젝트(Object)는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료구조, 함수 또는 메서드가 될 수 있다.

속성과 행동으로 구성된 모든 것.

* 속성 = 정보 = (변수)

* 행동 = 동작 = (함수-메서드)

* 클래스와 객체
  * 클래스(설계도) : 추상적인 정의, 설계 / 예) 가수, 강아지
    클래스를 만든다 == 타입을 만든다.
  * 객체(실제 사례) : 실제 하나의 사례, 예시 / 예) 이찬혁, 리트리버

* 객체와 인스턴스 : 클래스로 만든 객체를 인스턴스라고 함.
  객체는 클래스의 인스턴스(객체는 인스턴스 -> X)

* 파이썬은 모든 것이 객체(object) : 파이썬의 모든 것엔 속성과 행동이 존재

* 객체의 특징
  * 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  * 속성(attribute) : 어떤 상태(데이터)를 가지는가?
  * 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

  객체(object) = 속성(attribute) + 기능(method)

* 객체와 클래스 문법

  ```python
  # 클래스 정의 : 클래스만으로는 원하는 동작을 할 수 없음(설명을 적어놓은 것)
  class.myclass:
    pass

  # 인스턴스 생성
  myinstance = myclass()

  # 메서드 호출
  myinstance.mymethod()

  # 속성
  myinstance.myattribute
  ```

* 클래스와 인스턴스 : 객체의 설계도(클래스)를 가지고 객체(인스턴스)를 생성한다.

  * 클래스 : 객체들의 분류 / 설계도(class)

  * 인스턴스 : 하나하나의 실체 / 예) 인스턴스(instance)

* 객체의 비교

 * == : 동등한(equal) - 두 변수가 참조하는 객체가 동등한(내용이 같은)경우 True

 * is : 동일한(identical) - 두 변수가 동일한 객체를 가리키는 경우 True



### OOP의 속성

속성(정보) : 특정 테이터 타입/클래스의 객체들이 가지게 될 상태.데이터를 의미

   1. 인스턴스 변수 : 인스턴스가 개인적으로 가지고 있는 속성(attribute)(개인용)

       * 생정자 메서드(__int__)에서 self.<name>으로 정의

       * 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

   2. 클래스 변수 : 클래스 선언 내부에서 정의(공용)
       * <classname>.<name>으로 접근 및 할당

```python
class Circle():
  pi = 3.14 # 클래스 변수 정의

  def __init__(self, r):
    self.r = r # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 3.14

Circle.pi = 5 # 클래스 변수 변경
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5

C2.pi = 5 # 인스턴스 변수 변경
print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 5
```



### OPP의 메서드

메서드(행동) : 특정 데이터 타입 클래스의 객체에 공통적으로 적용 가능한 행위(함수)

1. 인스턴스 메서드 : 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드

   * 클래스 내부에 정의되는 메서드의 기본

     * 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

     ```python
     class myclass:
       def instance_method(self, arg1, ...):
     ```

   * self : 인스턴스 자기 자신
     * 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되도록 설계

   * 생성자 메서드(constructor method) : 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

   * 매직 메서드 : Duble underscore(_)가 있는 메서드 = 스페셜 메서드, 매직 메서드

     * 특정 상황에 자동으로 불리는 메서드

     * 예시

     ```python
     __str__(self) # 해당 객체의 출력형태를 지정
     __len__(self), __repr__(self)
     __it__(self, other), __le__(self, other), __eq__(self, other)
     __gt__(self, other) # 부등호 연산자(>, greater than)
     __ge__(self, other), __ne__(self, other)
     ```

     * 소멸자 메서드(destructor) 메서드 : 인스턴스 객체가 소멸(파괴)되기 직전 호출되는 메서드


2. 클래스 메서드 : 클래스가 사용할 메서드

   ```python
   class myclass:
   
      @classmethod
      def class_methon(cls, arg1, ...):
    
   myclass.class_methon(...)
   ```

   * 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여, @로 함수 위에 꾸밈

> 클래스 매서드와 인스턴스 메서드의 차이
> * 클래스 매서드 -> 클래스 변수 사용
> * 인스턴스 메서드 -> 인스턴스 변수 사용
> 
> 인스턴스 변수, 클래스 변수를 모두 사용하고 싶다면?
> * 클래스는 인스턴스 변수 사용이 불가능
> * 인스터스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능 

3. 스태틱(정적) 메서드 : 인스턴트 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용

   * @staricmethod 데코레이터를 사용하여 정의

   * 일반 함수처럼 작동하지만, 클래스 이름공간에 귀속됨.

   ```python
   class myclass:

   @staticmethod
   def static_method(arg1, ...):

   myclass.static_method(...)
   ```

* 인스턴스와 클래스 간의 이름공간(name space)
  
  * 클래스를 정의하면, 클래스와 해당하는 이름공간 생성

  * 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성

  * 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 클래스 순으로 탐색

### 객체지향의 핵심 4가지

1. 추상화 : 현실 세계를 프로그램 설계에 반영(복잡한 것은 숨기고, 필요한 것만 드러내기)
   
   1. 변수
   
   2. 함수
   
   3. 클래스

2. 상속 : 두 클래스 사이 부모-자식 관계를 적립
   
   * 모든 파이썬 클래스는 object를 상속 받음.
   
   ```python
   class childClass(parentClass):
   ```
   * 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속받음.
  
   * 상속 관련 함수와 메서드
   
   ```python
   isinstance(object, classinfo) # classinfo의 instance거나 subclass인 경우 True
   issubclass(class, classinfo) # class가 classinfo의 subclass면 True
   super() # 자식클래스에서 부모클래스를 사용하고 싶은 경우
   ```

   * 다중 상속 : 두개 이상의 클래스를 상속

     * 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

3. 다형성(Polymorphism) : 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음

   * 서로 다른 클래스에 속한 개체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음

   * 매서드 오버라이딩 : 상속받은 메서드를 재정의
     
     * 클래스 상솏, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경

     * 부모 클래스의 매서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용



4. 캡슐화 : 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단

   * 예시 : 주민등록번호

   * 파이썬에서 암묵적으로 존재하시만, 언어적으로는 존재하지 않음

   * 접근 제어자 종류
  
     1. Public Access Modifier

       * Public Member : 언더바 없이 시작하는 메서드나 속성

         * 어디서나 호출이 가능, 하위클래스 override 허용

         ```python
         def __init__(self, name, age):
           self.name = name
           self.age = 30
         ```

     2. Proteched Access Modifier

       * Protected Member : 언더바 1개로 시작하는 메서드나 속성

         * 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능

         * 하위 클래스 override 허용

         ```python
         def __init__(self, name, age):
           self.name = name
           self._age = 30

         def get_age(self):
           return self._age
         ```

     3. Private Access Modifier : 언더바 2개로 시작하는 메서드나 속성

       * 본 클래스 내부에서만 사용이 가능

       * 하위클래스 상속 및 호출 불가능, 외부 호출 불가능(오류)

       ```python
         def __init__(self, name, age):
           self.name = name
           self.__age = 30

         def get_age(self):
           return self.__age
         ```
     
   * getter 메서드와 setter 메서드 : 변수에 접근할 수 있는 메서드를 별도 생성

     * getter 메서드 : 변수의 값을 읽는 메서드 (@property 데코레이터 사용)

     * setter 메서드 : 변수의 값을 설정하는 성격의 메서드(@변수.setter 사용)

---

## 에러와 예외처리

### 디버깅

디버깅 ; 잘못된 프로그램을 수정하는 것

### 에러와 예외

* 문법 에러(Syntax Error) : 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어나갈 때 (parser) 문제가 발생할 위치를 표현

   * Invalid syntax : 문법 오류

   * assign to literal : 잘못된 할당

   * EOL(End of line)

   * EOF(End of file)

* 예외(Exception) : 실행도중 예상치 못한 상황을 맞이하면 프로그램 실행을 멈춤

   * ZeroDivisionError : 0으로 나누려고 할 때 발생

   * NameError : Name space상에 이름이 없을 경우

   * TypeError : 타입 불일치

   * ValueError : 타입은 올바르나 값이 적저라지 않거나 없는 경우

   * IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우

   * KeyError : 해당 키가 존재하지 않는 경우

   * ModuleNotFoundError : 없는 Module을 부르는 경우

   * ImprotError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

   * KeyboardInterrupt : 임의로 프로그램을 종료하였을 때

   * IndentationError : Indentation이 적절하지 않는 경우




### 예외 처리

* Try문 : 오류가 발생할 가능성이 있는 코드를 실행

### 예외 발생 시키기