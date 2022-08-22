class Node:
    def __init__(self, prev_ref=None, next_ref=None, data=None):
        self.prev_ref = prev_ref
        self.data = data
        self.next_ref = next_ref


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def createDLL(self, new_data):
        new_node = Node(data=new_data)
        new_node.next_ref = None
        new_node.prev_ref = None
        self.head = new_node
        self.tail = new_node
        print("The doubly linked list has been created.")

    def insertBeginning(self, new_data):
        new_node = Node(data=new_data)
        self.head.prev_ref = new_node
        new_node.next_ref = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Mentioned node doesn't exist")
            return

        next_node = prev_node.next_ref
        new_node = Node(data=new_data)
        prev_node.next_ref = new_node
        new_node.prev_ref = prev_node
        new_node.next_ref = next_node
        next_node.prev_ref = new_node

    def insertEnd(self, new_data):
        new_node = Node(data=new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while last_node.next_ref is not None:
            last_node = last_node.next_ref
        last_node.next_ref = new_node
        new_node.prev_ref = last_node
        self.tail = new_node

    def forwardTraversal(self):
        if self.head is None:
            print("The linked list does not exist.")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.data)
                temp_node = temp_node.next_ref

    def reverseTraversal(self):
        if self.head is None:
            print("The linked list does not exist.")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.data)
                temp_node = temp_node.prev_ref

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_ref


dll = DLL()
dll.createDLL(5)
dll.insertBeginning(9)
dll.insertEnd(10)
dll.insertEnd(11)
dll.reverseTraversal()
print([node.data for node in dll])
