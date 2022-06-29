# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            levLength = len(q)
            levNodes = []
            for i in range(levLength):
                node = q.popleft()
                if node:
                    levNodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levNodes:
                res.append(levNodes)
        return res

        