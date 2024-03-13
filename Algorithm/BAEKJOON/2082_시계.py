clockData = [
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
maxClockNum = [2, 9, 5, 9]
possibleNums = [set(range(10)) for _ in range(4)]

def CheckPossible(num: int, row: int, inputData: str):
    for i in range(3):
        if (inputData[i] == '#') & (clockData[num][row][i] == '.') :
            return False
    return True

for row in range(5):
    line = input().split(' ')
    for [idx, clockRow] in enumerate(line):
        for num in range(maxClockNum[idx] + 1):
            if (not CheckPossible(num, row, clockRow)) & (num in possibleNums[idx]): 
                possibleNums[idx].remove(num)

print(f'{min(possibleNums[0])}{min(possibleNums[1])}:{min(possibleNums[2])}{min(possibleNums[3])}')
