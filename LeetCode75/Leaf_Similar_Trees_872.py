# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2:
            return False

        return self.get_leap_nodes(root1, "") == self.get_leap_nodes(root2, "")

    def get_leap_nodes(self, root, leap_str=""):
        if not root:
            return leap_str
        if root.left is None and root.right is None:
            return leap_str + "," + str(root.val)
        else:
            return self.get_leap_nodes(root.left, leap_str) + self.get_leap_nodes(
                root.right, leap_str
            )
