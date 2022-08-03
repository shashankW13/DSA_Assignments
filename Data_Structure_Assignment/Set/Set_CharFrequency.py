# incomplete
from collections import Counter

string = 'xyyz'
str_list = []
temp_list = []
str_set = set()
res = False

for x in range(0, len(string)):
    str_set.add(string[x])
    str_list.append(string[x])

for y in str_set:
    temp_list = str_list[:]
    temp_list.remove(y)
    counter = Counter(temp_list)
    res = len(list(set(list(counter.values())))) == 1
    if res:
        print(f'Yes By removing at most one char {y} the frequency is same')
        break
    temp_list.clear()

if not res:
    print('No It is not possible to make frequency of each character same just by removing at most on character')

