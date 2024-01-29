# Definition for a binary tree node.

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        max_sum = float("-inf")  # Initialize to negative infinity
        max_level = 1
        current_level = 1
        queue = collections.deque([root])

        while queue:
            q_len = len(queue)
            current_sum = 0
            for i in range(q_len):
                node = queue.popleft()
                current_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = current_level

            current_level += 1
        return max_level


root = TreeNode(-100)

root.left = TreeNode(-200)
root.right = TreeNode(-300)

root.left.left = TreeNode(-20)
root.left.right = TreeNode(-5)

root.right.left = TreeNode(-10)


sol = Solution()
print(sol.maxLevelSum(root))
