# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = set()
        def in_order_traversal(root):
            if root:
                res.add(root.val)
                in_order_traversal(root.left)
                in_order_traversal(root.right)

        in_order_traversal(root)
        return sorted(list(res))[1] if len(res) >= 2 else -1