# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        q = collections.deque([root])
        res = []
        while q:
            mostRightSideNode = None
            qLenght = len(q)
            for i in range(qLenght):
                node = q.popleft()
                if node:
                    mostRightSideNode = node
                    q.append(node.left)
                    q.append(node.right)

            if mostRightSideNode:
                res.append(mostRightSideNode.val)

        return res