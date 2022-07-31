List = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
List1 = []

for x in range(len(List)):
    List1.append(round(List[x]))

print('Min number: ', min(List1))
print('Max number: ', max(List1))
List1.sort()

print('Result: ')
for x in range(len(List1)):
    print(List1[x] * 5, end=" ")
