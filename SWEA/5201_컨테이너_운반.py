for tc in range(int(input())):
    N, M = map(int, input().split())

    # 컨테이너와 트럭을 역순으로 정렬해서 입력받기(최대한 무거운 순서대로 옮길 수 있도록)
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    # 운반할 수 있는 컨테이너 선별하기
    ans = 0
    for truck in trucks:
        for weight, container in enumerate(containers):
            if truck >= container:              # 트럭이 컨테이너를 운반할 수 있다면
                ans += containers.pop(weight)   # 해당 컨테이너 무게를 정답에 더하기
                break

    print(f'#{tc + 1} {ans}')
