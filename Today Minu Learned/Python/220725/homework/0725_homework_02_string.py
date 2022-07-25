def count_vowels(word):
    return word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')

print(count_vowels('apple')) # => 2
print(count_vowels('banana'))  # => 3