# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def inventory_filter(item_type, inventory):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    dict_item = [] # 빈 리스트 생성
    for i in range(len(inventory)):
        if inventory[i]['type'] == item_type: # 아이템 타입이 맞다면
            dict_item.append(inventory[i]) # 빈 리스트에 추가
        else:
            pass
    
    return dict_item



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
