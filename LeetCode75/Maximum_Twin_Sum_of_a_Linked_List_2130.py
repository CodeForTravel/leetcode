# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# # Using hash table approach
# # ============================
# class Solution(object):
#     def pairSum(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: int
#         """

#         value_list = []

#         while head:
#             value_list.append(head.val)
#             head = head.next

#         l, r = 0, len(value_list) - 1
#         res = 0

#         while l < r:
#             res = max(res, value_list[l] + value_list[r])
#             l += 1
#             r -= 1
#         return res


# Approach: Reverse the second half of the linked list
def pairSum(self, head):
    slow, fast = head, head
    maxVal = 0

    # Get middle of linked list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse second part of linked list
    curr, prev = slow, None

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # Get max sum of pairs
    while prev:
        maxVal = max(maxVal, head.val + prev.val)
        prev = prev.next
        head = head.next

    return maxVal
