# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, max_val):
            if not root:
                return 0

            res = 1 if root.val >= max_val else 0
            max_val = max(root.val, max_val)
            res += dfs(root.left, max_val)
            res += dfs(root.right, max_val)
            return res

        return dfs(root, root.val)


root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.left = TreeNode(3)

root.right.left = TreeNode(1)
root.right.right = TreeNode(5)


sol = Solution()
print(sol.goodNodes(root))
