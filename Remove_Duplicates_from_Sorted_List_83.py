# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_tempt = head
        visited_list = []

        while head:
            visited_list.append(head.val)
            if head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                head = head.next
        return head_tempt
        
