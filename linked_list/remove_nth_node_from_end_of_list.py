# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        length = self.get_length(head)
        node_to_delete = length - n + 1
        current_position = 1
        current_node = head
        previous_node = None
        while current_node:
            if current_position == node_to_delete:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    head = current_node.next
                break

            previous_node = current_node
            current_node = current_node.next
            current_position += 1
        return head

    def get_length(self, head):
        current_node = head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length
