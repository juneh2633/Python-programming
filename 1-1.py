class Node:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, email):
        new_node = Node(name, email)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
       
        while current:
            print(f'["{current.name}", "{current.email}"]', end="")
            current = current.next
            if current:
                print(", ", end="")
        print("")

linked_list = LinkedList()

while True:
    name = input("이름--> ")
    if not name:
        break
    email = input("이메일--> ")
    linked_list.insert(name, email)
    linked_list.display()
