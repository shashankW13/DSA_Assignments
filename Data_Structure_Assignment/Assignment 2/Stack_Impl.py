class Stack:
    def __init__(self):
        self.stack = []

    # Check if the current stack is empty or not
    def isEmpty(self):
        if not self.stack:
            return 'Empty'
        else:
            return True

    # Return the size of the stack
    def size(self):
        if self.stack:
            return len(self.stack)
        else:
            return '0'

    # Push an element to the stack
    def push(self, element):
        self.stack.append(element)

    # Remove the last inserted element from the stack
    def pop(self):
        self.stack.pop()

    # Insert an element before an existing element
    def insert(self, index, element):
        self.stack.insert(self.stack.index(index), element)

    # Show all the elements in stack
    def show(self):
        for ele in self.stack:
            print(f'{ele} ->', end=" ")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(7)
stack.insert(2, 6)
print(stack.size())
stack.show()
