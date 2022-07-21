def get_strong_word(words_1, words_2):
    power_1 = 0 # 문자 힘 변수
    power_2 = 0


    for i in range(len(words_1)):
        words_1_1 = list(words_1) # 입력받은 문자를 리스트로 변환
        power_1 += ord(words_1_1[i]) # 첫번째 리스트 문자부터 숫자로 변환하여 변수에 누적

    
    for i in range(len(words_2)):
        words_2_2 = list(words_2) # 입력받은 문자를 리스트로 변환
        power_2 += ord(words_2_2[i]) # 첫번째 리스트 문자부터 숫자로 변환하여 변수에 누적

    print(words_1) if power_1 > power_2 else print(words_2) # 둘중 숫자가 더 높은 값을 출력

get_strong_word('z', 'a') # => ‘z’
get_strong_word('delilah', 'dixon') # => ‘delilah