def get_subseq(depth=0, subseq=[]):
    global max_num, max_list, min_num, min_list
    if depth == k + 1:
        subseq_num = int(''.join(map(str, subseq)))
        if max_num < subseq_num:
            max_num = subseq_num
            max_list = subseq[::]

        if subseq_num < min_num:
            min_num = subseq_num
            min_list = subseq[::]
        return
    
    for n in range(10):
        if visited[n] or (subseq and not check_sign(subseq[depth - 1], signs[depth - 1], n)):
            continue
        visited[n] = True
        subseq.append(n)
        get_subseq(depth + 1, subseq)
        subseq.pop()
        visited[n] = False

def check_sign(a, s, b):
    if s == '<':
        return a < b
    else:
        return a > b

visited, k, signs, max_num, max_list, min_num, min_list = [False] * 10, int(input()), list(input().split()), 0, [], 9999999999, []
get_subseq()
print(''.join(map(str, max_list)), ''.join(map(str, min_list)), sep='\n')