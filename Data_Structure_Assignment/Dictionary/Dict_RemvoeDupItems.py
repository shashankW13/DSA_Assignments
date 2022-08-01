from collections import Counter

random_dict = {'a': 2, 'b': 2, 'c': 4, 'd': 1, 'e': 1, 'f': 3, 'g': 4, 'h': 2, 'i': 5}
dup_values = []
new_dict = dict()

for k, v in random_dict.items():
    if v not in dup_values:
        dup_values.append(v)
        new_dict[k] = v

print(new_dict)
