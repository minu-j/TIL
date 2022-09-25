for tc in range(int(input())):
    N, M = map(int, input().split())

    queue = [M]
    count = 0
    visited = set()

    while N not in queue:
        for _ in range(len(queue)):
            now = queue.pop(0)
            if now not in visited and 0 < now <= 1000000:
                visited.add(now)
                if now % 2 == 0:
                    queue.append(now // 2)
                queue.append(now + 10)
                queue.append(now - 1)
                queue.append(now + 1)

                if N in queue:
                    break

        count += 1

    print(f'#{tc + 1} {count}')