# incomplete
string = 'xyyz'
str_list = []
temp_list = []
str_set = set()
count = []

for x in range(0, len(string)):
    str_set.add(string[x])
    str_list.append(string[x])

for y in str_set:
    temp_list = str_list[:]
    temp_list.remove(y)
    # if set(temp_list) == str_set:
    #     print(f'Yes By removing at most one char {y} the frequency is same')
    #     break
    count.append(temp_list.count(y))
    temp_list.clear()
# print('No It is not possible to make frequency of each character same just by removing at most on character')

ele = count[0]
for c in range(len(count)):
    if ele != count[c]:
        break
    elif c == len(count) - 1:
        print(1)

# print(str_set)
# print(temp_list)
# print(str_list)
print(count)
