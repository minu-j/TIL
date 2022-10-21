def self_number(n):
    num = n
    for _ in str(n):
        num += int(_)
    return num


print(self_number(33))
print(self_number(39))
print(self_number(51))
print(self_number(7521))