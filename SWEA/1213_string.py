for tc in range(10):
    N, target, string = int(input()), input(), input()

    ans = 0   # 정답의 갯수를 카운트할 변수 저장

    for i in range(len(string)):   # 전체 문자열의 길이만큼 반복
        if len(string[i:]) < len(target):   # 찾아야하는 문자열의 길이보다 남은 문자열 길이가 짧다면 반복문 종료
            break

        elif string[i] == target[0]:   # 찾아야 하는 문자열의 첫번째가 해당 문자와 같다면

            count = 0   # 카운트 초기화

            for j in range(len(target)):   # 찾아야하는 문자열의 길이만큼 반복
                if string[i + j] == target[j]:   # 몇개의 문자열이 일치하는지 확인해서
                    count += 1   # 카운트 + 1
                else:   # 찾던 중 다음 문자열이 찾아야하는 문자열과 다르다면 반복문 종료
                    break

            if count == len(target):   # 찾아야하는 문자열의 길이와, 일치하는 문자열의 갯수가 같다면
                ans += 1   # 정답 갯수 +1

    print(f'#{N} {ans}')