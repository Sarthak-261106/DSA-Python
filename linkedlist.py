class node():
    def __init__(self, value):
        self.val = value
        self.next = None

# head =node(1)
# head.next=node(2)
# head.next.next=node(3)

class linkedlist:
    head = None

    def printll(self):
        temp=self.head
        while temp!=0:
            print(temp.val, end="")
            temp=temp.next

    def inserttail(self, value):
        if self.head==None:
            self.head=node(value)
            return

        temp=self.head
        while temp.next!=None:
            temp=temp.next

        temp.next=node(value)    



            