FruitDict = {'Apple': 10, 'Banana': 5, 'Orange': 4, 'Guava': 6}
mult = 1

for fruit, values in FruitDict.items():
    mult *= values

print('Multiplied elements: ', mult)
