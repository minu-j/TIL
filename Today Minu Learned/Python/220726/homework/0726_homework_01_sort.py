# sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

list_1 = [6, 5, 4, 3, 2, 1]
list_1_sorted = sorted(list_1)

list_2 = [6, 5, 4, 3, 2, 1]
list_2_sorted = list_2.sort()

print(list_1) # [6, 5, 4, 3, 2, 1]
print(list_1_sorted) # [1, 2, 3, 4, 5, 6]
print(list_2) # [1, 2, 3, 4, 5, 6]
print(list_2_sorted) # None

# sorted() 함수는 일시적으로 리스트의 순서를 정렬하여 새로운 값을 만들고,
# .sort() 메서드는 리스트 자체의 순서를 변경시킨다.