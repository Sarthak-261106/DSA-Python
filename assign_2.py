# #Question:
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. 
# Note that pos is not passed as a parameter.
# Do not modify the linked list.

class Node():
    def __init__(self, value):
        self.val = value
        self.next = None
def detectCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
            return entry
    return None 

head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = third
result = detectCycle(head)

if result:
    print("Cycle starts at node:", result.val)
else:
    print("No cycle")