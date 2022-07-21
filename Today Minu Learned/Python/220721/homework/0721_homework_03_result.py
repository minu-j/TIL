def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)

print(result) 

# 결과 : None
# 이유 : c에 할당된 로컬값은 함수 내에서만 유효하기 때문에