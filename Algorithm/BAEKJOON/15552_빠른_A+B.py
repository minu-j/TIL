import sys

for tc in range(int(sys.stdin.readline())):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))