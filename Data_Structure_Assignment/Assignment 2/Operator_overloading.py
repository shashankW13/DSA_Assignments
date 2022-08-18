# + operator overloading
class AddMod:
    def __init__(self, obj1):
        self.obj1 = obj1

    # Overloading add operator
    def __add__(self, obj2):
        return f'Addition is:  {self.obj1 + int(obj2.obj1)}'


o1 = AddMod(1)
o2 = AddMod("2")

print(o1 + o2)


# > operator overloading
class GreaterMod:
    def __init__(self, obj1):
        self.obj1 = obj1

    # Overloading greater than operator
    def __gt__(self, other):
        if self.obj1 > int(other.obj1):
            return f'{self.obj1} is greater than {other.obj1}'
        else:
            return f'{other.obj1} is greater than {self.obj1}'


o1 = GreaterMod(5)
o2 = GreaterMod("7")

print(o1 > o2)
