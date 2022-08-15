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


# Checking subclass status
print('Is Teacher subclass of Staff?: ', issubclass(Teacher, Staff))
print('Is Staff subclass of Teacher?: ', issubclass(Staff, Teacher))
