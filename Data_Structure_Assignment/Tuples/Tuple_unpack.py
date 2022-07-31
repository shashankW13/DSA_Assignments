Random_Tuple = ('C++', 'Java', 1.23, 55, True)

(obj1, obj2, *obj3) = Random_Tuple

print('Unpacking tuple: ')
print(obj1)
print(obj2)
print(obj3, "\n")

str_tuple = ('Shashank', 'Wadekar', 'Zensar')
(name, surname, organization) = str_tuple
print('Unpacking tuple: ')
print(name)
print(surname)
print(organization, "\n")
