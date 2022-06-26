# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_length(root)
        
    def get_length(self, root, depth=0):
        if not root:
            return depth
        return max(self.get_length(root.left, depth + 1), self.get_length(root.right, depth + 1))
        