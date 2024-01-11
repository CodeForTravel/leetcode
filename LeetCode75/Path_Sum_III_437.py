class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def pathSum(self, root, sum):
        if root is None:
            return 0

        hash_map = {0: 1}
        self.findPathSum(root, 0, sum, hash_map)
        return self.total

    def findPathSum(self, curr, sum, target, hash_map):
        if curr is None:
            return

        sum += curr.val
        if sum - target in hash_map:
            self.total += hash_map[sum - target]

        hash_map[sum] = hash_map.get(sum, 0) + 1
        self.findPathSum(curr.left, sum, target, hash_map)
        self.findPathSum(curr.right, sum, target, hash_map)
        hash_map[sum] -= 1


root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.left = TreeNode(3)

root.right.left = TreeNode(1)
root.right.right = TreeNode(5)


targetSum = 7
sol = Solution()
print(sol.pathSum(root, targetSum))
