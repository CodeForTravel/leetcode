# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Preorder (Root, Left, Right) 
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def traversal(root):
            if not root:
                return
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res
        