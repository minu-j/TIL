from re import A


def duplicated_letters(letter):
    letter_list = sorted(list(letter)) # 문자열을 리스트로 변환
    answer = set() # 답을 모을 셋을 생성

    for i in range(len(letter_list)-1): # 리스트 마지막을 제외한 글자들 중
        if letter_list[i] == letter_list[i + 1]: # 해당하는 글자와 그 다음글자가 같다면?
            answer.add(letter_list[i]) # 셋에 해당 글자를 추가
    answer = sorted(list(answer)) # 만들어진 셋을 리스트로 변환
    return answer # 정답 리스트 반환

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))