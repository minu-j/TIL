def get_secret_number(words):
    words = list(words) # 입력받은 문자를 리스트로 변환
    ans = 0 # 정답 변수
    for i in range(len(words)):
        ans += ord(words[i]) # 첫번째 리스트 문자부터 숫자로 변환하여 변수에 누적
    print(ans) # 정답 출력

get_secret_number('happy') # => 546