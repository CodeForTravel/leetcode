# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# with BFS ===============
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_queue, res = [root], 0
        while len(node_queue):
            qlen, res = len(node_queue), 0
            for _ in range(qlen):
                visited_node = node_queue.pop(0)
                res += visited_node.val
                if visited_node.left:
                    node_queue.append(visited_node.left)
                if visited_node.right:
                    node_queue.append(visited_node.right)
        return res


# with DFS ===============
class SolutionD:
    def deepestLeavesSum(self, root):
        sum_ = []

        def dfs(root, lev):
            if lev == len(sum_):
                sum_.append(root.val)
            else:
                sum_[lev] += root.val

            if root.left:
                dfs(root.left, lev + 1)

            if root.right:
                dfs(root.right, lev + 1)

        dfs(root, 0)
        return sum_[-1]
