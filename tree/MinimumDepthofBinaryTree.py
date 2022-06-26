# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self,root):
        #Null node has 0 depth.
        if root == None:
            return 0

        # Leaf node reached.
        if not root.left and not root.right:
            return 1

        # Current node has only right subtree.
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # Current node has only left subtree.
        elif not root.right:
            return 1 + self.minDepth(root.left)
        
        # if none of the above cases, then recur on both left and right subtrees.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))