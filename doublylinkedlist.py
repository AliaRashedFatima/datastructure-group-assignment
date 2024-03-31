from node import Node
#Doubly link list class to access the data smoothly in system
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #append function to add details in class
    def append(self, data):
        new_node = Node(data)   #call Node class
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    #remove deatils from Doubly link list class
    def remove(self, key):
        current = self.head
        while current:
            if current.data.id == key:
                #remove previous data using condition
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False