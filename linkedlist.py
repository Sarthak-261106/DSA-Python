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

    def inserthead(self, value):
        if self.head==None:
            self.head=node(value)
            return

        temp=node(value)
        temp.next=self.head
        self.head=temp  

    def insertatk(self, value, k):
        if k==0:
            self.inserthead(value)
            return

        temp=self.head
        for i in range(k-1):
            temp=temp.next

        newnode=node(value)
        newnode.next=temp.next
        temp.next=newnode

    def deletion(self, k):
        if k==0:
            self.head=self.head.next
            return

        temp=self.head
        for i in range(k-1):
            temp=temp.next

        temp.next=temp.next.next

    def middle(self):
        lenght=0
        temp=self.head
        while temp!=None:
            lenght+=1
            temp=temp.next
        
        target=lenght//2+1
        count=0
        temp=self.head
        while count<target:
            temp=temp.next
            count+=1
        return temp    



            