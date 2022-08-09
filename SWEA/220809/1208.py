for i in range(10):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    while True:
        for j in range(len(boxes) - 1, 0, -1):   # 박스를 정렬
            for k in range(0, j):
                if boxes[k] > boxes[k + 1]:
                    boxes[k], boxes[k + 1] = boxes[k + 1], boxes[k]

        height_gap = boxes[-1] - boxes[0]   # 최고점과 최저점의 차를 변수에 할당

        if dump_count == 0 or height_gap <= 1:    # 남은 덤프 횟수가 0이 되거나 최고점과 최저점의 차가 1 이하가 되면
            print(f'#{i + 1} {height_gap}')       # 최고점과 최저점의 차를 출력
            break

        boxes[-1] -= 1    # 가장 높은 박스에서 1개를 빼고
        boxes[0] += 1     # 가장 낮은 박스에 1개를 더함
        dump_count -= 1   # 덤프 1개를 차감

