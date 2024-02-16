import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

def create_linked_list():
    numbers = random.sample(range(1, 46), 6)
    linked_list = LinkedList()
    for number in numbers:
        linked_list.append(number)
    return linked_list


linked_list = create_linked_list()
print( linked_list.display())