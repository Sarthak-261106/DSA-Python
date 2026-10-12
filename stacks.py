#LIFO

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items == []:
            return True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        if self.is_empty():
            return 0
        else:
            return len(self.items)