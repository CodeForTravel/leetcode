
# # Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        copyOfOldList = {None:None}

        current = head
        while current:
            copy_node = Node(current.val)
            copyOfOldList[current] = copy_node
            current = current.next

        current = head
        while current:
            copy_node = copyOfOldList[current]
            copy_node.next  = copyOfOldList[current.next]
            copy_node.random  = copyOfOldList[current.random]
            current = current.next

        return copyOfOldList[head]
        