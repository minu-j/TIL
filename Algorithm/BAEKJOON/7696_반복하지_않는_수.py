# 완전탐색
# n은 10^6보다 작으므로 완탐 가능
# ...한줄 알았는데, 중간에 미친듯이 중복되는 숫자들이 많이 나와서 그냥 완탐으로는 불가능

# while True:
#     N = int(input())
#     if not N:
#         exit(0)   # n == 0일 경우 프로그램 종료

#     ans = 0
#     while N:
#         ans += 1
#         print(ans)
#         # 해당 숫자 안에 반복되는 숫자가 있는지 확인
#         if len(set(str(ans))) == len(str(ans)):
#             N -= 1

#     print(ans)

# 그럼 그냥 다 구하고 N 인덱스 가져오자

from itertools import permutations

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_set = set()
for i in range(1, 9):   # N이 1000000까지라서 적절한 자리수까지만 구함, 다 구하면 메모리 초과
    num_set = num_set.union(
        map(lambda x: int(''.join(x)), permutations(nums, i)))
not_duplicated_nums = sorted(num_set)

while True:
    N = int(input())
    if not N:
        exit(0)   # n == 0일 경우 프로그램 종료
    else:
        print(not_duplicated_nums[N])
