# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    answer = '' # 답 문자열 생성
    code = list(word) # 단어의 리스트 생성
    for i in range(len(code)): 
        code[i] = ord(code[i]) # 단어 리스트를 아스키코드 숫자로 변환

    for i in range(len(code)):
        if chr(code[i]).isupper() == False: # 알파벳이 소문자라면
            code[i] += n # 숫자에 n을 더하고
            if code[i] > 122: # 122보다 클 때(알파벳 범위를 벗어날 때는)
                code[i] -= 26 # 26을 뺀다.
            else:
                continue
        else:
            code[i] += n
            if code[i] > 90:
                code[i] -= 26
            else:
                continue
    
    for i in range(len(code)): # 코드 리스트를 답 문자열에 문자열 형태로 변환
        answer += chr(code[i])

    return answer

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx