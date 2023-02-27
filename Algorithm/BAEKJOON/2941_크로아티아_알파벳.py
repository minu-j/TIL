alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = list(input())  # 최대 3자리까지 확인해야 하므로 문자열 리스트 뒤에 2개 항목 추가
word.append('')
word.append('')

ans = 0

for i in range(len(word)):   # 입력받은 문자열만큼 반복
    for j in range(len(alphabet)):   # 크로아티아 알파벳 목록만큼 또한번 반복
        if word[i] == alphabet[j][0]:   # 해당 문자열과 크로아티아 알파벳 첫번째 글자가 동일할 때
            count = 0   # 일단 카운트를 0으로 만들어놓고
            for k in range(len(alphabet[j])):   # 해당 크로아티아 알파벳의 길이만큼 반복
                if word[i + k] == alphabet[j][k]:   # 크로아티아 알파벳 글자들이 입력받은 문자열의 뒷부분과 동일하다면
                    count += 1   # 카운트 +1
            if count == len(alphabet[j]):   # 카운트가 크로아티아 알파벳 글자 길이와 같다면
                ans += 1   # 정답 문자 한개 추가
                for _ in range(len(alphabet[j])):   # 정답카운트 올린 크로아티아 알파벳만큼은 제거
                    word[i + _] = ''

ans += len(''.join(word))   # 크로아티아 문자열을 뺀 나머지 알파벳의 갯수도 정답에 포함

print(ans)