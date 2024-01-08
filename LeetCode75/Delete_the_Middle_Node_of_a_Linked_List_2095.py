# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return None

        slow = head  # This will be the middle node after loop is end, and we need to remove it
        fast = head
        before_middle = None  # to remove the middle node we need to tract the node just before the middle

        while fast and fast.next:
            before_middle = slow
            slow = slow.next
            fast = fast.next.next

        # Removing the middle value
        before_middle.next = slow.next
        return head
