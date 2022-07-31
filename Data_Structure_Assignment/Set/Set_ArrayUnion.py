# n = input('Enter number of arrays to add: ')
# arr = []

# for x in range(int(n)):
#     ele = []
#     m = input('Enter array size: ')
#     for y in range(0, int(m)):
#         ele.append(int(input()))
#     arr.append(ele)

arr_set = set()
arr = [
    [1, 2, 2, 4, 3, 6],
    [5, 1, 3, 4],
    [9, 5, 7, 1],
    [2, 4, 1, 3]
]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        arr_set.add(arr[x][y])

print(arr_set)
# print(arr)