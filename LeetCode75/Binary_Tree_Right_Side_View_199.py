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

        res = []
        queue = collections.deque([root])

        while queue:
            current_q_len = len(queue)
            right_most_node_of_queue = None

            for i in range(current_q_len):
                node = queue.popleft()
                if node:
                    right_most_node_of_queue = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_most_node_of_queue:
                res.append(right_most_node_of_queue.val)
        return res
