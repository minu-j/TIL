from re import A


def low_and_up(letter):
    letter_list = list(letter) # 문자열을 리스트로 변환
    for i in range(len(letter_list)):
        if i % 2 != 0:
            letter_list[i] = letter_list[i].upper()
    letter = ''
    for _ in range(len(letter_list)):
        letter += letter_list[_]
    return letter

print(low_and_up('apple'))
print(low_and_up('banana'))