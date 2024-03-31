#Stack class is used to maintain prescription records    
class Stack:
    def __init__(self):
        self.items = []

    #push the data in stack
    def push(self, item):
        self.items.append(item)

    #pop(delete) data from stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    #to check whether stack is empty or not
    def is_empty(self):
        return len(self.items) == 0