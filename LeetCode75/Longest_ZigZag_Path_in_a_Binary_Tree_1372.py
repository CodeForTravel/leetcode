# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(
            self.find_zigzag_depth(root.left, True, 0),
            self.find_zigzag_depth(root.right, False, 0),
        )

    def find_zigzag_depth(self, root, is_left, depth):
        if not root:
            return depth

        if is_left:
            depth = max(
                depth,
                self.find_zigzag_depth(root.right, False, depth + 1),
                self.find_zigzag_depth(root.left, True, 0),
            )
        else:
            depth = max(
                depth,
                self.find_zigzag_depth(root.left, True, depth + 1),
                self.find_zigzag_depth(root.right, False, 0),
            )
        return depth
