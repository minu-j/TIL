# 코드는 딕셔너리로 구조화
code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(int(input())):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    passcode = []        # 이진수 암호코드를 저장

    # 위아래 의미없는 줄 전부 지우고, 암호코드에 해당하는 행이 나오면 2진수 암호코드 리스트에 저장
    for i in matrix:
        if '1' not in i:
            continue
        else:
            passcode = ''.join(i)
            break

    # 이진수 암호코드는 무조건 1로 끝나고, 길이는 56이므로
    # 뒤에서부터 확인했을 때 1이 나오는 값부터 56개의 값만 남긴다.
    for j in range(M - 1, -1, -1):
        if passcode[j] == '1':
            passcode = passcode[j - 55:j + 1]   # 암호를 확인했으면 변수에 저장 후 반복문 종료
            break

    ans = 0     # 정답을 저장할 변수
    odd = 0     # 홀수번호를 저장할 변수
    even = 0    # 짝수번호를 저장할 변수

    # 전체 이진수 암호코드를 7단위로 순회하면서 암호코드에 맞는 숫자 찾기
    for idx, k in enumerate(range(0, 56, 7)):
        ans += code[passcode[k:k + 7]]          # 일단 정답 변수에 더하고,
        if (idx + 1) % 2 == 1:                  # 해당 자리수 홀/짝에 따라 홀/짝 번호 변수에 각각 저장
            odd += code[passcode[k:k + 7]]
        else:
            even += code[passcode[k:k + 7]]

    if (odd * 3 + even) % 10 != 0:      # 조건을 만족하지 않으면 정답은 0으로 출력
        ans = 0

    print(f'#{tc + 1} {ans}')
