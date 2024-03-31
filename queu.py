from collections import deque

#Queue class to maintain the appointment data
class Queue:
    def __init__(self):
        self.items = deque()

    #enqueue(insert) data in queue
    def enqueue(self, item):
        self.items.append(item)

    #dequeue data from queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return None

    #remove data from queueu
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False

    #to check the queue is empty or not    
    def is_empty(self):
        return len(self.items) == 0

    #display the details of patient
    def display(self):
        for item in self.items:
            print("ID:", item.id, "Name:", item.name, "Condition:", item.condition)

