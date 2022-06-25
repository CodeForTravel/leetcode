# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, current = None, head
        while current:
            print(current)
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

