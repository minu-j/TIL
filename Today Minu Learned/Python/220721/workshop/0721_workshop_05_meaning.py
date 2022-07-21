def get_secret_word(nums):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 알파벳 대문자 문자열
    abc = list(abc) # 알파벳 대문자의 문자열을 리스트로 변환
    sabc = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 소문자 문자열
    sabc = list(sabc) # 알파벳 소문자의 문자열을 리스트로 변환
    word = ''
    key_number = 0
    key_word = ''

    for i in range(len(nums)): # 제시되는 숫자 리스트의 길이만큼 반복
        num = nums[i] # 첫번째 리스트 값부터 num에 할당

        if 90 >= num >= 65: # 90이하, 65이상이면 대문자
            key_number = num-65 # 65를 빼서 아스키 코드 숫자를 대문자 리스트 숫자와 맞춤
            key_word = abc[key_number] # 키워드 변수에 해당 알파벳을 할당 -> 21

        elif 122 >= num >= 97: # 122이하, 97이상이면 소문자
            key_number = num-97 # 97를 빼서 아스키 코드 숫자를 소문자 리스트 숫자와 맞춤
            key_word = sabc[key_number] # 키워드 변수에 해당 알파벳을 할당 -> 21
        word += key_word # 위에서 정해진 알파벳을 변수에 할당
    print(word)

get_secret_word([83, 115, 65, 102, 89]) # => ‘SsAfY