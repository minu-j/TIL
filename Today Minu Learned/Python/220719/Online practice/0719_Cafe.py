orders = ['아이스아메리카노', '카라멜마키야또', '에스프레소', '아메리카노', '아메리카노', '아이스라떼', '핫초코', '아이스아메리카노', '아메리카노', '아이스카라멜마키야또', '아이스라떼', '라떼마키야또', '카푸치노', '라떼마키야또']

print('총 주문 건 수 : ', len(orders)) # 총 주문 건 수

orders_set = set(orders) # set에 메뉴 list 저장하여 중복 제거
orders = list(orders_set) # set으로 중복 제거된 목록을 list로 저장
orders.sort(reverse=True) # list에 저장된 항목을 내림차순으로 정렬

print('중복을 제거한 메뉴 : ', orders) # 중복을 제거한 메뉴