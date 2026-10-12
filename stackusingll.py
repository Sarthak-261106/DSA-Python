class node:
    def __init__(self,val):
        self.val=val
        self.next=None

class stackusingll:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False

    def push(self,val):
        newnode=node(val)
        newnode.next=self.head
        self.head=newnode

    def pop(self):
        if self.is_empty():
            return None
        else:
            temp=self.head
            self.head=self.head.next
            return temp.val

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.val

    def size(self):
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            temp=temp.next
        return count      
