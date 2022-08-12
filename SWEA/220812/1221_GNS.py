num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(T):
    tc_num, tc_len = input().split()
    string = list(input().split())

    count_list = [0] * 10   # 카운팅 정렬을 이용하기로 했어요
    for i in string:
        for j in range(len(num)):
            if i == num[j]:   # 만약 해당 문자가 num 리스트의 문자와 같다면
                count_list[j] += 1   # num 리스트 문자의 위치를 기반으로 카운트

    print(tc_num)
    for i in range(10):
        for j in range(count_list[i]):
            print(num[i], end=' ')

'''
버블정렬로도 풀어봤는데.. 컴퓨터가 멈춥니다ㅋㅋㅋㅋㅋ

    for _ in range(len(string)):
        for i in range(len(string) - 1):
            now_num = next_num = 0

            for j in range(len(num)):

                if string[i] == num[j]:
                    now_num = j

                if string[i + 1] == num[j]:
                    next_num = j

            if now_num > next_num:
                string[i], string[i + 1] = string[i + 1], string[i]
'''