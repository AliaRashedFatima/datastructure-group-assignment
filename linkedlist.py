from node import Node
#Singly link list Class to use Node to add details
class LinkedList:
    def __init__(self):
        self.head = None

    #add details function in linked list
    def append(self, data):
        new_node = Node(data)   #call Node class to add data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    #delete details from linked list function        
    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                #use condition to remove previous data
                if current.prev: 
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False