def solution(s):
    num_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = list(s)

    for i in range(len(s)):   # brute force로 냅다 풀기
        for j in range(len(num_eng)):
            if num[i] == num_eng[j][0]:
                count = 0
                for k in range(len(num_eng[j])):
                    if num[i + k] == num_eng[j][k]:
                        count += 1
                if count == len(num_eng[j]):
                    num[i] = str(j)
                    for _ in range(1, len(num_eng[j])):
                        num[i + _] = ''

    return ''.join(num)

print(solution('one4seveneight'))