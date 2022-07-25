def get_dict_avg(get_dict_avg):
    return sum(get_dict_avg.values()) / len(get_dict_avg)


print(get_dict_avg({
               'python' : 80,
               'web' : 83,
               'algorithm' : 90,
               'django' : 89,
})) # 85.5