# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        slowPointer, fastPointer = head, head.next

        #finding the middle pointer
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        #reversing the 2nd half of the list
        current = slowPointer.next
        prev = slowPointer.next = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        #merging the first and 2nd half of the list
        firstHead, secondHead  = head, prev
        while secondHead:
            temp1, temp2 = firstHead.next, secondHead.next

            firstHead.next = secondHead
            secondHead.next = temp1
            firstHead, secondHead = temp1,temp2





        
# creating node
node1 = ListNode(1,None)
node2 = ListNode(2,None)
node1.next = node2

node3 = ListNode(3,None)
node2.next = node3

node4 = ListNode(4,None)
node3.next = node4

node5 = ListNode(5,None)
node4.next = node5

node5.next = None


#Testing Node ====================
obj = Solution()
obj.reorderList(node1)

print(node1.val)

node2 = node1.next
print(node2.val)

node3 = node2.next
print(node3.val)

node4 = node3.next
print(node4.val)

node5 = node4.next
print(node5.val)