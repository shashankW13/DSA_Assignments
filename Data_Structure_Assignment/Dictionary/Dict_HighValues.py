from collections import Counter

random_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 1}

c = Counter(random_dict)

max_values = c.most_common(3)

print('Max 3 values: ')
for x in max_values:
    print(x)
