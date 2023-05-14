day = ['FRI','SAT', 'SUN','MON','TUE','WED','THU']
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    accDay = b
    for m in range(a - 1):
        accDay += month[m]
    return day[accDay % 7 - 1]