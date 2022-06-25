# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.merge_tow_sorted_list(l1,l2))
            lists = merged_lists
        return lists[0]

    def merge_tow_sorted_list(self,list1,list2):
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
        