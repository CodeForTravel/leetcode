# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1
class Solution(object):
    def hasCycle(self, head):
        hashSet = set()
        
        while head:
            if head in hashSet:
                return True
            else:
                hashSet.add(head)
            head = head.next
        return False

# Solution 2
class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

     


        
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

node5.next = None


#Testing Node ====================
obj = Solution()
print(obj.hasCycle(node1))

# print(node1.val)

# node2 = node1.next
# print(node2.val)

# node3 = node2.next
# print(node3.val)

# node4 = node3.next
# print(node4.val)

# node5 = node4.next
# print(node5.val)