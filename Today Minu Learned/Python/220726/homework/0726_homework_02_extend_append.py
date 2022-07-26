# .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

list_1 = []
list_2 = []

x = 'python'
y = [1, 2, 3, 4, 5]

list_1.extend(x)
list_1.extend(y)

list_2.append(x)
list_2.append(y)

print(list_1) # ['p', 'y', 't', 'h', 'o', 'n', 1, 2, 3, 4, 5]
print(list_2) # ['python', [1, 2, 3, 4, 5]]

# .extend()는 각각의 interable한 객체를 리스트 뒤에 추가하고,
# .append()는 입력받은 내용을 리스트 끝에 그대로 넣는다.