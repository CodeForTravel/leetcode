# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_node = ListNode()
        current_node = new_node

        carray = 0
        while l1 or l2 or carray:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            sum_value = value1 + value2 + carray
            carray = sum_value // 10
            sum_value = sum_value % 10

            current_node.next = ListNode(sum_value)
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_node.next


# l1_node1 = ListNode(3)
# l1_node2 = ListNode(4, l1_node1)
# l1_node3 = ListNode(2, l1_node2)

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# obj = Solution()

# print(obj.addTwoNumbers(l1, l2))
