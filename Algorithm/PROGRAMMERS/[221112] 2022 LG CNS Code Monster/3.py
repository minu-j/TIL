def solution(reference, track):
    def jump(depth, score):
        nonlocal answer

        if depth == len(track):
            if min(score) > answer:
                answer = min(score)
            return

        for i in range(depth, len(track)):
            if track[depth:i + 1] in set_reference:

                score.append(len(track[depth:i + 1]))
                jump(depth + len(track[depth:i + 1]), score)
                score.pop()

        score.append(1)
        jump(depth + 1, score)
        score.pop()

    set_reference = []
    for i in range(len(reference)):
        for j in range(i, len(reference)):
            set_reference.append(reference[i:j + 1])

    answer = 0

    jump(0, [])

    return answer


print(solution("abc", "bcab"))              # 2
print(solution("vxrvip", "xrviprvipvxrv"))  # 4