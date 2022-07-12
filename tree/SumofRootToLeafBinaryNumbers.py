# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path_stack = []
        res = [0]

        def calculate_path(root):
            if not root:
                return

            path_stack.append(root)
            # checking if leaf node
            if not root.left and not root.right:
                binary_str = "".join([str(i.val) for i in path_stack])
                res[0] += int(binary_str,2)

            calculate_path(root.left)
            calculate_path(root.right)
            path_stack.pop()

        calculate_path(root)

        return res[0]
        