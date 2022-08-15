class Teacher:

    # Initializing Private variable
    __sal = None

    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.__sal = sal

    # Private function displaying private variable 'sal'
    def __display_info(self):
        return self.name + ' ' + self.age, self.__sal

    # Function accessing the private function to display the details
    def display_details(self):
        return self.__display_info()


t1 = Teacher('Shashank', 'Wadekar', 20000)
print(t1.display_details())
