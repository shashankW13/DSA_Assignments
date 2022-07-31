List = ['Shadow', 'Zensar', 'Python']
n = 6

for x in range(len(List)):
    if len(List[x]) > 6:
        print(List[x])
    elif x == len(List) - 1:
        print('Nothing')
        