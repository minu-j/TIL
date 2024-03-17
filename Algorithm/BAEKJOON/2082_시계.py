clock_data = [  # 시계 데이터
    ['###', '#.#', '#.#', '#.#', '###'],
    ['..#', '..#', '..#', '..#', '..#'],
    ['###', '..#', '###', '#..', '###'],
    ['###', '..#', '###', '..#', '###'],
    ['#.#', '#.#', '###', '..#', '..#'],
    ['###', '#..', '###', '..#', '###'],
    ['###', '#..', '###', '#.#', '###'],
    ['###', '..#', '..#', '..#', '..#'],
    ['###', '#.#', '###', '#.#', '###'],
    ['###', '#.#', '###', '..#', '###']
]
max_clock_num = [2, 9, 5, 9]    # 시계의 자리별 최대값
possible_nums = [set(range(10)) for _ in range(4)]  # 각 자리별 들어갈 수 있는 숫자 set


# 특정 숫자가 들어갈 수 있는지 확인하는 함수
def check_possible(num: int, row: int, input_data: str):
    for i in range(3):
        if (input_data[i] == '#') & (clock_data[num][row][i] == '.'):
            return False
    return True


# 시계의 각 줄을 입력받으며 자리별 불가능한 숫자들 골라내기
for row in range(5):
    line = input().split(' ')
    for [idx, clockRow] in enumerate(line):
        for num in range(max_clock_num[idx] + 1):
            if (not check_possible(num, row, clockRow)) & (num in possible_nums[idx]):
                possible_nums[idx].remove(num)

print(
    f'{min(possible_nums[0])}{min(possible_nums[1])}:{min(possible_nums[2])}{min(possible_nums[3])}')
