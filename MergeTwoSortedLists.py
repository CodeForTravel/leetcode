class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        cur_node = dummy_node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next = list1
                cur_node = list1
                list1 = list1.next

            else:
                cur_node.next = list2
                cur_node = list2
                list2 = list2.next

        if list1 or list2:
            cur_node.next = list1 if list1 else list2
        return dummy_node.next
