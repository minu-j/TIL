heap = ['최소힙:']


def heap_push(item):
    heap.append(item)

    child = len(heap) - 1
    parent = child // 2

    # 루트 노드 일 경우, 위가 더 작을 경우 반복문 종료
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]   # swap
        child = parent
        parent = child // 2


def heap_pop():
    if len(heap) == 1:
        return

    result = heap[1]

    item = heap.pop()
    heap[1] = item

    parent = 1           # 루트부터 시작하니까 1
    child = parent * 2   # 왼쪽이 더 작다고 가정하자

    if child + 1 <= len(heap) - 1:           # chile+1이 heap 범위 내에 있고,
        if heap[child] > heap[child + 1]:    # 왼쪽 자식노드가 오른쪽 자식노드보다 값이 크다면
            child += 1                       # 오른쪽 자식노드를 선택

    while child <= len(heap) - 1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2

        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1

    return result
