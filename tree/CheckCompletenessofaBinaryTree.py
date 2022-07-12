# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque([root])
        prev_node = root
        while q:
            
            cur_node = q.popleft()
            if cur_node:
                if not prev_node:
                    return False
                q.append(cur_node.left)
                q.append(cur_node.right)
            prev_node = cur_node
        return True

