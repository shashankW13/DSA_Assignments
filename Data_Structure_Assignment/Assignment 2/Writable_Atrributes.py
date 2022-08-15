# Parent Class
class Staff:

    # Initializing constructor
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # Display staff information
    def staff_info(self):
        return f'Name: {self.fname} {self.lname}'


# Child class
class Teacher(Staff):

    # Overriding parent class's constructor and adding new parameters
    def __init__(self, fname, lname, sal, role):
        super().__init__(fname, lname)
        self.sal = sal
        self.role = role

    # Display staff information along with new data
    def staff_info(self):
        return f'Name: {self.fname} {self.lname}' + '\n' \
               + f'Salary: {self.sal} ' + f'Role: {self.role}'


staff1 = Teacher('Shashank', 'Wadekar', 100000, 'Teacher')
print('Writable attributes: ')
print('fname:', staff1.fname)
print('lname:', staff1.lname)
print('sal:', staff1.sal)
print('role:', staff1.role)
