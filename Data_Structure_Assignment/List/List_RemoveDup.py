List = [1, 2, 3, 1, 2, 3, 3, 3, 'a', 'a', 'b']
remove_dup = []

for x in range(len(List)):
    if List[x] not in remove_dup:
        remove_dup.append(List[x])

print(List)
print(remove_dup)