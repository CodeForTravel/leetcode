# Definition for singly-linked list.
from operator import truediv


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1
class Solution(object):
    def detectCycle(self, head):
        hashSet = set()

        current = head
        while current:
            if current in hashSet:
                return current
            else:
                hashSet.add(current)
            current = current.next


        if current is None:
            return None
        


     
# creating node
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

node3 = ListNode(3)
node2.next = node3

node4 = ListNode(4)
node3.next = node4

node5 = ListNode(5)
node4.next = node5

node5.next = node2


#Testing Node ====================
obj = Solution()
print(obj.detectCycle(node1))

# print(node1.val)

# node2 = node1.next
# print(node2.val)

# node3 = node2.next
# print(node3.val)

# node4 = node3.next
# print(node4.val)

# node5 = node4.next
# print(node5.val)