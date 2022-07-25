def only_square_area(num1, num2):
    
    area = set() # 중복 제거를 위해 set 활용
    for x in range(len(num1)): # 너비와 높이를 2차원으로 한번씩 곱셈
        for y in range(len(num2)):
            if num1[x] == num2[y]: # 너비와 높이가 같을 경우
                a = num1[x] * num2[y] # 두 숫자의 곱을
                area.add(a) # 셋에 추가
            else:
                pass

    
    return area

print(only_square_area([32, 55, 63], [13, 32, 40, 55])) # => [1024, 3025])