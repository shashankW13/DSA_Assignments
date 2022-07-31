New_Tuple = (1, 2, 3, 1, 2, 3, 1, 1, 1, 3, 3, 4, 4, 4, 4, 'a', 'b', 'a')
count = 1
duplicate = set()

for x in range(len(New_Tuple)):
    if New_Tuple.count(New_Tuple[x]) > 1:
        duplicate.add(New_Tuple[x])

print(duplicate)
