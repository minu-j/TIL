def count_blood(blood):
    dict_blood = {'A': blood.count('A'), 'B': blood.count('B'), 'AB': blood.count('AB'), 'O': blood.count('O')}
    return dict_blood

print(count_blood([
               'A', 'B', 'A', 'O', 'AB', 'AB',
               'O', 'A', 'B', 'O', 'B', 'AB',
])) # 85.5